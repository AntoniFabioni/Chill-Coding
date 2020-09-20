'''
This program plots the current along a transmission line with respect to the
z-coordinate and time. Two plots are produced, each at a different time.
'''

import numpy as np
import matplotlib.pyplot as plt

a = np.log(np.sqrt(10/3))

def i(z,t):

    return np.exp(-a*z)*np.cos(6*np.pi*10**9*t - 8*np.pi*z)

zs = np.linspace(0, 0.5, 100)

ys0 = i(zs, 0)
ys1 = i(zs, 0.5*10**(-9))

plt.plot(zs, ys0, color='cornflowerblue', label='i(z, 0)')
plt.plot(zs, ys1, color='tomato', label='i(z, 0.5ns)')
plt.legend(loc='upper right')
plt.xlabel('z Position (m)')
plt.ylabel('Current (A)')
plt.title('Current Over First 2 Wavelengths at t = 0 and t = 0.5ns')
plt.show()