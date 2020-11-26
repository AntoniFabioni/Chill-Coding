'''
This program plots H-field along a solenoid's z-axis.
'''

import numpy as np
import matplotlib.pyplot as plt

def H(z):

    return 12*abs(((10-z)/np.sqrt((10-z)**2+25))+((10+z)/np.sqrt((10+z)**2+25)))

zs = np.linspace(-20, 20, 41)

vs = H(zs)

plt.plot(zs, vs, '.', color='purple')

plt.xlabel('Position along Solenoid (cm)')
plt.ylabel('Magnitude of H-Field (kA/m)')
plt.title('Magnitide of H-Field VS Position Along Axis of Solenoid')
plt.show()