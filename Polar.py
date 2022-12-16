import numpy as np
import matplotlib.pyplot as plt

k = 15
N = np.linspace(0, 1, k)
M = np.radians(np.linspace(0,360, k))

# Grid
r, theta = np.meshgrid(N, M)
values = np.random.choice([-1,0,1], size = (M.size, N.size))

# Set axes projection as polar
# plt.axes(projection = 'polar')
fig, ax = plt.subplots(subplot_kw = dict(projection = 'polar'), figsize = (10,10))
polar = ax.contourf(theta, r, values)
plt.colorbar(polar, shrink = 0.5, aspect = 6)









## setting the radius
#r = 10
#  
## creating an array containing the radian values
#rads = np.arange(0, (2 * np.pi), 0.01)
#  
## plotting the circle
#for rad in rads:
#    plt.polar(rad, r, 'g.')
#  
## display the Polar plot
#plt.show()