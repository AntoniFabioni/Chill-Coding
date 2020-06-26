'''
This program simulates the motion of a double
pendulum system in 2 dimensions.

This code was sourced from Matplotlib.org,
the specific goal here is to make it run
in real time.
'''


from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

G = 9.8     # acceleration due to gravity, in m/s^2
L1 = 1.4    # length of pendulum 1 in meters
L2 = 0.9    # length of pendulum 2 in meters
M1 = 1.0    # mass of pendulum 1 in kg
M2 = 1.1    # mass of pendulum 2 in kg

th1 = 120.0 # initial angle of pendulum 1 (degrees)
th2 = -10.0 # initial angle of pendulum 2 (degrees)
w1 = 0.0    # initial angular velocity of pendulum 1 (degrees per second)
w2 = 0.0    # initial angular velocity of pendulum 2 (degrees per second)

# create a time array sampled at "dt" second long steps
dt = 0.02
t = np.arange(0, 20, dt)

# initial state
state = np.radians([th1, w1, th2, w2])

def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

# num1 = -G * (2 * M1 + M2) * sin(th1)
# num2 = -M2 * G * sin(th1 - 2 * th2)
# num3 = -2 * sin(th1 - th2) * M2
# num4 = w2**2 * L2 + w1**2 * L1 * cos(th1 - th2)
# den = L1 * (2 * M1 + M2 - M2 * cos(2 * th1 - 2 * th2))
# a1 = (num1 + num2 + num3*num4) / den

# num1 = 2 * sin(th1 - th2)
# num2 = w1**2 * L1 * (M1 + M2)
# num3 = G * (M1 + M2) * cos(th1)
# num4 = w2**2 * L2 * M2 * cos(th1 - th2)
# den = L2 * (2 * M1 + M2 - M2 * cos(2 * th1 - 2 * th2))
# a2 = num1 * (num2 + num3 + num4) / den

# w1 += a1
# w2 += a2
# th1 += w1
# th2 += w2

# y = 

# x1 = L1 * sin(th1)
# y1 = -L1 * cos(th1)

# x2 = L2 * sin(th2) + x1
# y2 = -L2 * cos(th2) + y1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-(L1+L2), L1+L2), ylim=(-(L1+L2), L1+L2))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text


ani = animation.FuncAnimation(fig, animate, range(1, len(y)),
                              interval=dt*1000, blit=True, init_func=init)
plt.show()
print(y)