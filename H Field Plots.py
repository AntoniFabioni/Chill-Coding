'''
This program plots H-field along a solenoid's central axis (z-axis).
'''

import numpy as np
import matplotlib.pyplot as plt

def H(z):
    return 12*abs(((10-z)/np.sqrt((10-z)**2+25))+((10+z)/np.sqrt((10+z)**2+25)))

bounds = (-20, 20)
res = max(bounds) - min(bounds) + 1 # the "+ 1" includes 0 in the domain.

zs = np.linspace(bounds[0], bounds[1], res)

hs = H(zs)

colour = 'teal'

plt.plot(zs, hs, '-', color=colour)

plt.xlabel('Position along Solenoid (cm)')
plt.ylabel('Magnitude of H-Field (kA/m)')
plt.title('Magnitide of H-Field VS Position Along Axis of Solenoid')
plt.show()