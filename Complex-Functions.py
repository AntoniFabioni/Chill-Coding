# Complex Funnptions

import matplotlib.pyplot as plt
import numpy as np
import seaborn


vx = np.complex(1, 0)
vy = np.complex(2, 0)

v_in = (vx, vy)

def RootNot(u):
    avg = (u[0] + u[1])/2
    diff = (u[0] - u[1])/2
    return (np.complex(avg, diff), np.complex(avg, -diff))

v_out = RootNot(v_in)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(vx.real, vx.imag, 'bo')
axs[0, 0].set_title('Input: x-component')
axs[0, 1].plot(vy.real, vy.imag, 'go')
axs[0, 1].set_title('Input: y-component')
axs[1, 0].plot(v_out[0].real, v_out[0].imag, 'bx')
axs[1, 0].set_title('Output: x-component')
axs[1, 1].plot(v_out[1].real, v_out[1].imag, 'gx')
axs[1, 1].set_title('Output: y-component')


plt.show()