'''
This program plots H-field (aka magnetic field) along a solenoid's central axis (z-axis).
'''

import numpy as np
import matplotlib.pyplot as plt

def H(z):
    return 12*abs(((10-z)/np.sqrt((10-z)**2+25))+((10+z)/np.sqrt((10+z)**2+25)))

bounds = (-20, 20)
resolution = max(bounds) - min(bounds) + 1 # the "+ 1" includes 0 in the domain.

zs = np.linspace(bounds[0], bounds[1], resolution)

hs = H(zs)

colour = 'cornflowerblue'

plt.plot(zs, hs, '-', color=colour) # Canadian spelling :)

plt.xlabel('Position along Solenoid (cm)')
plt.ylabel('Magnitude of H-Field (kA/m)')
plt.title('Magnitide of H-Field VS Position Along Axis of Solenoid')
plt.show()