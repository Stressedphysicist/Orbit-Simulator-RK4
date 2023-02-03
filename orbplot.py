import numpy as np
import matplotlib.pyplot as plt

def proyplot( rs, args ):
	_args = {
		'figsize'      : ( 15, 5 ),
		'labels'       : [ '' ] * len( rs ),
		'colors'       : [ 'm', 'c', 'r', 'C3' ],
		'traj_lws'     : 3,
		'dist_unit'    : 'AU',
		'groundtracks' : False,
		'cb_radius'    : 0,
		'cb_SOI'       : None,
		'cb_SOI_color' : 'c',
		'cb_SOI_alpha' : 0.7,
		'cb_axes'      : True,
		'cb_axes_mag'  : 2,
		'cb_cmap'      : 'YlOrRd',
		'cb_axes_color': 'w',
		'axes_mag'     : 0.8,
		'axes_custom'  : None,
		'title'        : 'Trajectories',
		'legend'       : True,
		'axes_no_fill' : True,
		'hide_axes'    : False,
		'azimuth'      : False,
		'elevation'    : False,
		'show'         : False,
		'filename'     : False,
		'dpi'          : 300
	}

	
	#plt.style.use( 'dark_background' )

	for key in args.keys():
		_args[ key ] = args[ key ]

	fig = plt.figure( figsize = _args[ 'figsize' ] )
	ax  = fig.add_subplot( 121, projection = '3d'  )
	ay  = fig.add_subplot( 122 )

	max_val = 0
	n       = 0

	for r in rs:
		ax.plot( r[ :, 0 ], r[ :, 1 ], r[:,2],
			color = _args[ 'colors' ][ n ], label = _args[ 'labels' ][ n ],
			zorder = 10, linewidth = _args[ 'traj_lws' ] )
		ax.plot( [ r[ 0, 0 ] ], [ r[ 0 , 1 ] ], [ r[ 0 , 2 ] ], 'o',
			color = _args[ 'colors' ][ n ] )		

		max_val = max( [ r.max(), max_val ] )
		n += 1

	_u, _v = np.mgrid[ 0:2*np.pi:20j, 0:np.pi:20j ]
	_x     = _args[ 'cb_radius' ] * np.cos( _u ) * np.sin( _v )
	_y     = _args[ 'cb_radius' ] * np.sin( _u ) * np.sin( _v )
	_z     = _args[ 'cb_radius' ] * np.cos( _v )
	ax.plot_surface( _x, _y, _z, cmap = _args[ 'cb_cmap' ], zorder = 1 )

	if _args[ 'cb_axes' ]:
		l       = _args[ 'cb_radius' ] * _args[ 'cb_axes_mag' ]
		x, y, z = [ [ 0, 0, 0 ], [ 0, 0, 0  ], [ 0, 0, 0 ] ]
		u, v, w = [ [ l, 0, 0 ], [ 0, l, 0 ], [ 0, 0, l ] ]
		ax.quiver( x, y, z, u, v, w, color = _args[ 'cb_axes_color' ] )

	xlabel = 'X (%s)' % _args[ 'dist_unit' ]
	ylabel = 'Y (%s)' % _args[ 'dist_unit' ]
	zlabel = 'Z (%s)' % _args[ 'dist_unit' ]

	if _args[ 'axes_custom' ] is not None:
		max_val = _args[ 'axes_custom' ]
	else:
		max_val *= _args[ 'axes_mag' ]

	ax.set_xlabel( xlabel )
	ax.set_ylabel( ylabel )
	ax.set_zlabel( zlabel )
	ax.set_box_aspect( [ 1, 1, 1 ] )
	ax.set_aspect( 'auto' )

	if _args[ 'azimuth' ] is not False:
		ax.view_init( elev = _args[ 'elevation' ],
					  azim = _args[ 'azimuth'   ] )
	
	if _args[ 'axes_no_fill' ]:
		ax.w_xaxis.pane.fill = False
		ax.w_yaxis.pane.fill = False
		ax.w_zaxis.pane.fill = False		

	if _args[ 'hide_axes' ]:
		ax.set_axis_off()

	max_val = 0
	n       = 0

	for r in rs:
		ay.plot( r[ :, 0 ], r[ :, 1 ],
			color = _args[ 'colors' ][ n ], label = _args[ 'labels' ][ n ],
			zorder = 10, linewidth = _args[ 'traj_lws' ] )
		ay.plot( [ r[ 0, 0 ] ], [ r[ 0 , 1 ] ], 'o',
			color = _args[ 'colors' ][ n ] )			

		max_val = max( [ r.max(), max_val ] )
		n += 1

	if _args[ 'axes_custom' ] is not None:
		max_val = _args[ 'axes_custom' ]
	else:
		max_val *= _args[ 'axes_mag' ]

	xlabel = 'X (%s)' % _args[ 'dist_unit' ]
	ylabel = 'Y (%s)' % _args[ 'dist_unit' ]

	ay.set_xlabel( xlabel )
	ay.set_ylabel( ylabel )

	if _args['title']:
		fig.suptitle(_args['title'])

	if _args[ 'filename' ]:
		plt.savefig( _args[ 'filename' ], dpi = _args[ 'dpi' ] )
		print( 'Saved', _args[ 'filename' ] )

	if _args[ 'show' ]:
		plt.show()
	
	plt.close()
	
	
def proyplot2(states,names):
    plt.figure(figsize=(10,7))
    plt.xlabel('X (AU)')
    plt.ylabel('Y (AU)')
    plt.plot(0, 0, marker="o", markersize=0.4, markeredgecolor="red", markerfacecolor="yellow", label='sun')
    n = 0

    for state in states:
        rs = [state]

        for r in rs:
            plt.plot( r[ :, 0 ], r[ :, 1 ] , label= names[n] )
            plt.plot( [ r[ 0, 0 ] ], [ r[ 0 , 1 ] ])
        
        n += 1 

    plt.legend()
    plt.show()

def polarconvert(rs):
    rho = np.sqrt(rs[0]**2 + rs[1]**2)
    phi = np.arctan2(rs[1], rs[0])
    return np.array([rho,phi])

def polargrapher(rs):
    
    fig = plt.figure(figsize = ( 15, 3 ))
    (arho, aphi) = fig.subplots(1, 2)
    ncount = 0
    Npoint = []
    rhos = []
    phis = []

    for r in rs:
        rhos.append(r[0])
        phis.append(r[1])
        Npoint.append(ncount)
        ncount += 1

    phis_degree = [((phi/np.pi) * 180) for phi in phis]
    arho.plot(rhos)
    arho.set_title('radius')
    arho.set_ylabel( 'radius (AU)' )
    arho.set_xlabel( 'time (days)' )
    
    aphi.plot(phis_degree)
    aphi.set_ylabel( 'angle (degrees)' )
    aphi.set_xlabel( 'time (days)' )
    aphi.set_title('angle')

    aphi.grid(visible=True,which='both',axis='both')
    arho.grid(visible=True,which='both',axis='both')
     
    plt.show()


def statesAU(state):
    AU  = 1.496e11
    coords = state[ :3 ]
    stateAU = coords/AU
    return np.array( [ stateAU[ 0 ], stateAU[ 1 ], stateAU[ 2 ],
			 state[ 3 ], state[ 4 ], state[ 5 ] ] )