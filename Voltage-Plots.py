'''
This program plots AC voltage as a function of time.
'''

import numpy as np
import matplotlib.pyplot as plt

def v(t):

    return 56*np.cos(2*np.pi*60*t)

ts = np.linspace(0, 1/30, 100)

vs = v(ts)

plt.plot(ts, vs, color='cornflowerblue')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('AC Voltage Over First 2 Periods')
plt.show()