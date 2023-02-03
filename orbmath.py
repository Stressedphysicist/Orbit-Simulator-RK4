import numpy as np

# Unidades y valores
sun = [1.99e30]
m = sun[0]
AU = 1.496e11  # m
G = 6.67408e-11  # m3 kg-1 s-2
yr = 3.154e+7  # seconds
day = 86400  # seconds
G = 6.67408e-11  # m3 kg-1 s-2
alph = 1.1e-8
e = 0.206  # eccentricity
sma = 0.39*AU  # semi-major axis
x0 = (1+e)*sma
v0 = np.sqrt(((G*m)/sma)*((1-e)/(1+e)))


def two_body_ode_mod(t, state):
    '''
    Newtons Universal Law of Gravitation

    State is an array in the form of [x,y,z,vx,vy,vz]

    Returns an array in the form of [vx,vy,vz,ax,ay,az]
    '''
    r = state[:3]
    a = -(G*m) * r / np.linalg.norm(r) ** 3

    return np.array([state[3], state[4], state[5],
                     a[0], a[1], a[2]])


def rk4_step(f, t, y, h):
    '''
    Calculate one RK4 step
    '''
    k1 = f(t, y)
    k2 = f(t + 0.5 * h, y + 0.5 * k1 * h)
    k3 = f(t + 0.5 * h, y + 0.5 * k2 * h)
    k4 = f(t + h, y + k3 * h)

    return y + h / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)


def mercury_correction(t, state):
    r = state[:3]
    a = (-G*m)*(r / np.linalg.norm(r) ** 3)*(1+(alph/np.linalg.norm(r)**2))

    return np.array([state[3], state[4], state[5],
                     a[0], a[1], a[2]])
