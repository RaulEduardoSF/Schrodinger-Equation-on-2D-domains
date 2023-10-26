import numpy as np
import scipy.sparse as sparse
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter

plt.style.use(['seaborn-dark'])
font = {'family': 'serif',
        'color': 'black',
        'weight': 'normal',
        'size' : 16,
        }

N = 200                # Mallado finito
a = -1
b = 1
X, Y = np.meshgrid(np.linspace(a, b, N, dtype=float),
                   np.linspace(a, b ,N, dtype=float))

#def potential(x,y):
#       return 1E-3/(np.sqrt(x**2 + y**2))**2
# Dipolo eléctrico
#def potential(x,y):
#       mu_CO = 0.12
#       mu_H2O = 1.83
#       epsilon = 8.85E-12
#       return 2*mu_CO*mu_CO/(4*np.pi*epsilon*(np.sqrt(x**2 + y**2))**3)

pot = np.zeros((N,N), dtype = float)

def potential(pot):
       alpha = 0.4
       delta = 50
       pot[int(N/2 - delta), int(N/2)] = -alpha
       pot[int(N/2 + delta ), int(N/2)] = -alpha
       pot[int(N/2), int(N/2 - delta)] = -alpha
       pot[int(N/2), int(N/2 + delta)] = -alpha
       pot[int(N/2), int(N/2)] = -alpha
       return pot
""" Graficando el Potencial """

# fig, ax = plt.subplots(figsize = (10,8))
# ax.set_title('Potencial en $[{},{}]$'. format(a,b), fontdict = font)
# graph_V = ax.contourf(potential(pot), levels = 20, cmap = 'magma')
# plt.colorbar(graph_V, shrink = 0.5, aspect = 5)
# plt.show(graph_V)

"""____________________________________________________________________________

DIFERENCIAS FINITAS
____________________________________________________________________________"""
V = potential(pot)

diag = np.ones([N])
diags = np.array([diag, -2*diag, diag])
D = sparse.spdiags(diags, np.array([-1,0,1]), N, N)
T = -1/2 * sparse.kronsum(D,D)
U = sparse.diags(V.reshape(N**2), (0))
H = T+U

eigenvalues, eigenvectors = eigsh(H, k = 11, which='SM')
def get_e(n):
    return eigenvectors.T[n].reshape((N,N))

"""____________________________________________________________________________
3D Surface
****************************************************************************"""
state = 7

fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={"projection":"3d"})
ax.set_title('Distribución de probabilidad $|\\Psi(x,y)|^2$\n $n_x = {}$, $n_y = {}$'. format(state,state), fontdict = font)
ax.set_zlabel('|$\\Psi|^2$', fontdict = font)
ax.set_xlabel('$x$', fontdict = font)
ax.set_ylabel('$y$', fontdict = font)
surf = ax.plot_surface(X, Y, get_e(state)**2, cmap='magma',
                   linewidth=0, antialiased=False)
plt.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

fig, ax = plt.subplots(figsize = (13,9))
ax.set_title('Distribución de probabilidad $|\\Psi(x,y)|^2$\n $n_x = {}$, $n_y = {}$'. format(state,state), fontdict = font)
ax.imshow(get_e(state)**2, cmap = 'magma')
ax.set_xlabel('$x$', fontdict = font)
ax.set_ylabel('$y$', fontdict = font)
plt.colorbar(surf, shrink = 0.5, aspect = 6)

# YlOrRd


"""____________________________________________________________________________
3D Animation
****************************************************************************"""
#my_cmap = plt.get_cmap()
#def init():
#    # Plot the surface.
#    ax.plot_surface(X, Y, get_e(0)**2, cmap=my_cmap,
#                       linewidth=0, antialiased=False)
#    ax.set_xlabel('$x/a$')
#    ax.set_ylabel('$y/a$')
#    ax.set_zlabel('$\propto|\psi|^2$')
#    return fig,
#
#def animate(i):
#    ax.view_init(elev=10, azim=4*i)
#    return fig,
#
#fig = plt.figure()
#ax = Axes3D(fig)
#ani = animation.FuncAnimation(fig, animate, init_func=init,
#                               frames=90, interval=50)
#ani.save('rotate_azimuth_angle_3d_surf.gif',writer='pillow',fps=20)
#
#alpha = eigenvalues[0]/2
#E_div_alpha = eigenvalues/alpha
#_ = np.arange(0, len(eigenvalues), 1)
#plt.scatter(_, E_div_alpha)
#[plt.axhline(nx**2 + ny**2,color='r') for nx in range(1,5) for ny in range(1,5)]
