'''Vizualize Complex Functions (Root of Not)'''

import matplotlib.pyplot as plt
import numpy as np

i = complex(0, 1)

# Parametric path for x-coordinate
def rx(t):
    return np.cos(t) + i*np.sin(t)

# Parametric path for y-coordinate
def ry(t):
    return t - i

t_start, t_stop, number_of_points = 0, 1, 100

def RootNot(u):
    avg = (u[0] + u[1])/2
    diff = (u[0] - u[1])/2
    return (complex(avg, diff), complex(avg, -diff))

fig, axs = plt.subplots(2, 2)

for t in np.linspace(t_start, t_stop, number_of_points):

    vx = rx(t)
    vy = ry(t)
    
    axs[0, 0].plot(vx.real, vx.imag, 'bo')
    axs[0, 1].plot(vy.real, vy.imag, 'go')

    v_out = RootNot((vx, vy))

    axs[1, 0].plot(v_out[0].real, v_out[0].imag, 'bx')
    axs[1, 1].plot(v_out[1].real, v_out[1].imag, 'gx')

axs[0, 0].set_title('Input: x-component')
axs[0, 1].set_title('Input: y-component')
axs[1, 0].set_title('Output: x-component')
axs[1, 1].set_title('Output: y-component')

axs[0, 0].set_xlabel("Real")
axs[0, 0].set_ylabel("Imaginary")
axs[0, 1].set_xlabel("Real")
axs[0, 1].set_ylabel("Imaginary")
axs[1, 0].set_xlabel("Real")
axs[1, 0].set_ylabel("Imaginary")
axs[1, 1].set_xlabel("Real")
axs[1, 1].set_ylabel("Imaginary")

plt.show()



# # Complex Functions

# import matplotlib.pyplot as plt

# vx = complex(1, 0)
# vy = complex(2, 0)

# v_in = (vx, vy)

# def RootNot(u):
#     avg = (u[0] + u[1])/2
#     diff = (u[0] - u[1])/2
#     return (complex(avg, diff), complex(avg, -diff))

# v_out = RootNot(v_in)

# fig, axs = plt.subplots(2, 2)

# axs[0, 0].plot(vx.real, vx.imag, 'bo')
# axs[0, 0].set_title('Input: x-component')

# axs[0, 1].plot(vy.real, vy.imag, 'go')
# axs[0, 1].set_title('Input: y-component')

# axs[1, 0].plot(v_out[0].real, v_out[0].imag, 'bx')
# axs[1, 0].set_title('Output: x-component')

# axs[1, 1].plot(v_out[1].real, v_out[1].imag, 'gx')
# axs[1, 1].set_title('Output: y-component')

# plt.show()