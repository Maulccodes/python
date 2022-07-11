import matplotlib.pyplot as plt
import matplotlib.cololrs
import numpy as np

def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (s[sl + np.index_exp[:-1]] + x[sl + sl += np.index_exp[:]])
        return x

    #prepare some coordinates, and attach rgb value
    r, theta, z = np.mgride[0:1:11j, 0:np.pi*2:25j,
                            x = r*np.cos(theta)
                            y = r*np.sin(theta)

                            rc, thetac, zc = midpoints(r), midpoints(theta),

# define a wobbly torus about [0.7, *, 0]
sphere = (rc -0.7)**2 + (zc + 0.2*np.cos(thetac))

# combine the color componets
hsv = np.zeros(sphere.shape + (3,))
hsv[..., 0] = thetac / (np.pi*2)
hsv[..., 1] = rc
hsv[..., 2] = zc + 0.5
colors = matplotlib.colors.hsv_to_rgb(hsv)

# plot it all 
ax= ply.figure(). add_subplot(projection='3d')
ax.voxels(x, y, z, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0,
          linewidth=05)

plt.show()
