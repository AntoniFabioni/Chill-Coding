'''
This program uses the Fast Fourier Tramsform to decompose
a time-varying signal into its respective frequencies.
'''

import numpy as np
import numpy.fft as FFT
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

# Signal
def f(t):
    return (np.sin(50 * 2 * np.pi * t) + 0.5 * np.sin(75 * 2 * np.pi * t) - 0.75 * np.sin(150 * 2 * np.pi * t)) * 20 * np.exp(-(t ** 2))

# Number of samples
N = 600

# Sample spacing
T = 1.0 / 800.0

# Input / Output lists
x = np.linspace(0.0, N*T, N)
y = f(x)

# Transformed x and y
xf = np.linspace(0.0, 1.0//(2.0*T), N//2)
yf = FFT.fft(y)

# Positive real output
Y = 2.0/N * np.abs(yf[0:N//2])

# Plot of transformed f(t) with local maxima highlighted
plt.plot(xf, Y)
plt.plot(xf[argrelextrema(Y, np.greater)], Y[argrelextrema(Y, np.greater)], 'mo')

plt.grid()
plt.show()