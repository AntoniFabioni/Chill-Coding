'''
This program plots AC voltage as a function of time.
'''

import numpy as np
import matplotlib.pyplot as plt

def v(t):

    return 56*np.sin(2*np.pi*60*t)

ts = np.linspace(0, 1/30, 100)

vs = v(ts)

plt.plot(ts, vs, color='darkorange')

plt.plot(0, 0, '.', color='chocolate')
plt.text(0, 0,'(0 s, 0.0 V)')

plt.plot(1/4*1/60, 56, '.', color='chocolate')
plt.text(1/4*1/60, 56,'(1/240 s, 56.0 V)')
plt.plot(1/2*1/60, 0, '.', color='chocolate')
plt.text(1/2*1/60, 0,'(1/120 s, 0.0 V)')
plt.plot(3/4*1/60, -56, '.', color='chocolate')
plt.text(3/4*1/60, -56,'(1/80 s, -56.0 V)')
plt.plot(1/60, 0, '.', color='chocolate')
plt.text(1/60, 0,'(1/60 s, 0.0 V)')

plt.plot(5/4*1/60, 56, '.', color='chocolate')
plt.text(5/4*1/60, 56,'(1/48 s, 56.0 V)')
plt.plot(6/4*1/60, 0, '.', color='chocolate')
plt.text(6/4*1/60, 0,'(1/40 s, 0.0 V)')
plt.plot(7/4*1/60, -56, '.', color='chocolate')
plt.text(7/4*1/60, -56,'(1/34 s, -56.0 V)')
plt.plot(1/30, 0, '.', color='chocolate')
plt.text(1/30, 0,'(1/30 s, 0.0 V)')

plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('AC Voltage Over First 2 Periods')
plt.show()