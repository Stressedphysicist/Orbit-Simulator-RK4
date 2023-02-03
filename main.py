import numpy as np
import matplotlib.pyplot as plt

from orbplot import *
from orbmath import *


# Unidades
AU = 1.496e11  # m
G = 6.67408e-11  # m3 kg-1 s-2
yr = 3.154e+7  # seconds
day = 86400  # seconds

# Astronomic Data written as [Mass,Distance-From-Sun,velocity,Period] (kg,m,m/s,years)
# Data retrieved from https://nssdc.gsfc.nasa.gov/planetary/factsheet/

sun = [1.99e30]
mercury = [3.303e23,   5.79e10,  47400, 2.4085e-1]
venus = [4.870e24,   1.08e11,  35000, 6.1521e-1]
earth = [5.976e24,   1.49e11,  29800, 1.0]
mars = [6.418e23,   2.28e11,  24100, 1.88089]
jupiter = [1.899e27,   7.78e11,  13100, 1.18622e1]
saturn = [5.686e26,   1.43e12,  9700, 2.94577e1]
uranus = [8.66e25,   2.86e12,  6800, 8.40139e1]
neptune = [1.030e23,   4.51e12,  5400, 1.64793e2]
pluto = [1e22,   5.90e12,  4700, 2.47686e3]
m = sun[0]


def proyecto(planet, radius, velocity, period, dt):
    statei = [radius, 0, 0, 0, velocity, 0]
    tspan = period * yr
    steps = int(tspan / dt)
    ets = np.zeros((steps, 1))
    states = np.zeros((steps, 6))  # Inicializa array [0,0,0,0,0,0]
    polars = np.zeros((steps, 2))
    AU_states = np.zeros((steps, 6))
    states[0] = statei

    for step in range(steps - 1):
        states[step + 1] = rk4_step(
            two_body_ode_mod, ets[step], states[step], dt)

    counter = 0

    for state in states:
        AU_states[counter] = statesAU(state)
        counter += 1

    counter = 0

    for state in AU_states:
        rs = np.array([state[0], state[1]])
        polars[counter] = polarconvert(rs)
        counter += 1

    return states, AU_states, polars, planet


def mercury_proyecto(planet, radius, velocity, period, dt):
    statei = [radius, 0, 0, 0, velocity, 0]
    tspan = period * yr
    steps = int(tspan / dt)
    ets = np.zeros((steps, 1))
    states = np.zeros((steps, 6))  # Inicializa array [0,0,0,0,0,0]
    polars = np.zeros((steps, 2))
    AU_states = np.zeros((steps, 6))
    states[0] = statei

    for step in range(steps - 1):
        states[step + 1] = rk4_step(
            mercury_correction, ets[step], states[step], dt)

    counter = 0

    for state in states:
        AU_states[counter] = statesAU(state)
        counter += 1

    counter = 0

    for state in AU_states:
        rs = np.array([state[0], state[1]])
        polars[counter] = polarconvert(rs)
        counter += 1

    return states, AU_states, polars, planet
