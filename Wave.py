'''
This program displays an animation of an oscillating wave u(x,t).
'''

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use('dark_background')

fig = plt.figure()
fig.set_dpi(300)
ax1 = fig.add_subplot(1, 1, 1)

# Wave speed
c = 1

# x-axis
xdomain = (-pi, pi)
x0 = np.linspace(xdomain[0], xdomain[1], 10000)

# Initial time
t0 = 0

# Time increment
dt = 0.05

# Wave to be plotted
def u(x, t):
    return (np.cos(x + 3*c*t)**2 + np.cos(x - 2*c*t)**2)

a = []
for i in range(500):
    U = u(x0, t0)
    t0 += dt
    a.append(U)

k = 0
def animate(i):
    global k
    x = a[k]
    k += 1
    ax1.clear()
    plt.plot(x0, x, color='cornflowerblue')
    plt.grid(True)
    plt.ylim((-2, 2))
    plt.xlim(xdomain)

anim = animation.FuncAnimation(fig, animate, interval=17)
plt.show()