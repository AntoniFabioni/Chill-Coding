# This program is under construction.

import numpy as np
import matplotlib.pyplot as plt

def f(x, r):
    
    return r * x * (1 - x)

def iterate(start, n, r):

    ans = start

    for i in range(n):

        ans = f(ans, r)

    return ans

r = np.linspace(0, 4, 15000)

limit = [iterate(0.5, 100, i) for i in r]

plt.plot(r, limit, '-', color='slategrey')
plt.title('$x_{n + 1} = rx_{n}(1 - x_{n})$', fontsize=20)
plt.xlabel('r', fontsize=15)
plt.ylabel('$Limit_{n → ∞}$', fontsize=15) 
plt.show()