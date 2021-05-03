'''Vizualize Complex Functions ("root of not" operation on a qubit)'''

import matplotlib.pyplot as plt
import numpy as np

# Ignore warnings in console
from matplotlib.axes._axes import _log as matplotlib_axes_logger
matplotlib_axes_logger.setLevel('ERROR')
 
i = complex(0, 1)

# Parametric path for x-coordinate
def rx(t):
    return np.cos(t) + i*np.sin(t)

# Parametric path for y-coordinate
def ry(t):
    return (1 + i)*t**2 - t/(2 - 3*i) + (2 - i)

t_start, t_stop, number_of_points = 0, 1, 500

def RootNot(u):
    avg = (u[0] + u[1])/2
    diff = (u[0] - u[1])/2
    return (complex(avg, diff), complex(avg, -diff))

fig, axs = plt.subplots(2, 2)

vx_real = [rx(t).real for t in np.linspace(t_start, t_stop, number_of_points)]
vy_real = [ry(t).real for t in np.linspace(t_start, t_stop, number_of_points)]

vx_imag = [rx(t).imag for t in np.linspace(t_start, t_stop, number_of_points)]
vy_imag = [ry(t).imag for t in np.linspace(t_start, t_stop, number_of_points)]

vx_out = [RootNot((vx_real[t] + i*vx_imag[t], vy_real[t] + i*vy_imag[t]))[0] for t in range(number_of_points)]
vy_out = [RootNot((vx_real[t] + i*vx_imag[t], vy_real[t] + i*vy_imag[t]))[1] for t in range(number_of_points)]

grad1 = [(0, 0.5, n/number_of_points) for n in range(number_of_points)]
grad2 = [(0.6, 0.1, n/number_of_points) for n in range(number_of_points)]
size = 3

for n in range(number_of_points):

    axs[0, 0].scatter(vx_real[n], vx_imag[n], c=grad1[n], s=size)
    axs[0, 1].scatter(vy_real[n], vy_imag[n], c=grad2[n], s=size)

    axs[1, 0].scatter(vx_out[n], vx_out[n], c=grad1[n], s=size)
    axs[1, 1].scatter(vy_out[n], vy_out[n], c=grad2[n], s=size)

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


''' OLD CODE BELOW ... NOT USED IN FINAL PROGRAM '''

# for t in np.linspace(t_start, t_stop, number_of_points):

#     vx = rx(t)
#     vy = ry(t)
    
#     axs[0, 0].plot(vx.real, vx.imag, 'bo')
#     axs[0, 1].plot(vy.real, vy.imag, 'go')

#     v_out = RootNot((vx, vy))

#     axs[1, 0].plot(v_out[0].real, v_out[0].imag, 'bx')
#     axs[1, 1].plot(v_out[1].real, v_out[1].imag, 'gx')

# axs[0, 0].plot(vx_real, vx_imag, linewidth=2)
# axs[0, 1].plot(vy_real, vy_imag, linewidth=2)

# axs[1, 0].plot(vx_out, vx_out, linewidth=2)
# axs[1, 1].plot(vy_out, vy_out, linewidth=2)





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