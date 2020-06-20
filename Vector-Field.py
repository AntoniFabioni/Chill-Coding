'''
This program has the goal of displaying a vector field
corresponding to a given differential equation.

Note that unit vectors will be displayed.
'''

import numpy as np
import matplotlib.pyplot as plt

rangex, rangey = 20, 20

density = 40

x, y = np.meshgrid(np.linspace(-rangex, rangex, density), np.linspace(-rangey, rangey, density))

dx = 1
dy = 3*np.sin(x)-2*np.cos(y)

unit_dx = dx/np.sqrt(dx**2 + dy**2)
unit_dy = dy/np.sqrt(dx**2 + dy**2)

plt.quiver(x, y, unit_dx, unit_dy)
plt.show()