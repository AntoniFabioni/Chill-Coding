'''
This program uses the Fast Fourier Tramsform to decompose
a time-varying signal into its respective frequencies.
'''

import numpy as np
import numpy.fft as FFT

# Test

input = [np.sin(np.radians(t)) for t in range(361)]

output = FFT.fft(input)
print(output)