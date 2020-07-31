'''
This program uses the Fast Fourier Tramsform to decompose
a time-varying signal into its respective frequencies.

The output is a side-by-side comparison of the original
graph and its transform.
'''

import numpy as np
import numpy.fft as FFT
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

# Signal
def f(t):
    g1 = np.sin(50 * 2 * np.pi * t) + 0.5 * np.sin(75 * 2 * np.pi * t) - 0.75 * np.sin(150 * 2 * np.pi * t)
    g2 = 10 * np.exp(-t ** 2)
    g3 = np.cos(np.pi / 3 * t) - np.log10(2 * t + 10)
    return 2 * g1 * (g2 + g3)

# Number of samples
N = 2000

# Sample spacing
T = 1.0 / 1000.0

# Input / Output lists
x = np.linspace(0.0, N*T, N)
y = f(x)

# Transformed x and y
xf = np.linspace(0.0, 1.0//(2.0*T), N//2)
yf = FFT.fft(y)

# Positive real output
Y = 2.0/N * np.abs(yf[0:N//2])

# Plot of f(t) and FFT{f(t)} with local maxima highlighted in the latter.
fig, axs = plt.subplots(2)
fig.tight_layout(pad=2.0)

axs[0].plot(x, y, color='cornflowerblue')
axs[0].set_title('f(t)')

axs[1].plot(xf, Y, color='cornflowerblue')
axs[1].set_title('FFT{f(t)}')
plt.plot(xf[argrelextrema(Y, np.greater)], Y[argrelextrema(Y, np.greater)], 'k.')

plt.grid()
plt.show()
