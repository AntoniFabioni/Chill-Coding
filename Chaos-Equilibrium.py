# This program is under construction.

import numpy as np
import matplotlib.pyplot as plt

# def f(x, r):
    
#     return r * x * (1 - x)

# def iterate(start, n, r):

#     ans = start

#     for i in range(n):

#         ans = f(ans, r)

#     return ans

# r = np.linspace(0, 4, 15000)

# limit = [iterate(0.5, 500, i) for i in r]

# plt.plot(r, limit, '-', color='slategrey')
# plt.title('$x_{n + 1} = rx_{n}(1 - x_{n})$', fontsize=20)
# plt.xlabel('r', fontsize=15)
# plt.ylabel('$Limit_{n → ∞}$', fontsize=15) 
# plt.show()

rs = np.linspace(1, 4, 1000)

N = 500
x = 0.5 + np.zeros(N)
endcap = np.arange(round(N * 0.9), N)

for ri in range(len(rs)):

    for n in range(N - 1):
        x[n + 1] = rs[ri] * x[n] * (1 - x[n])
    
    u = np.unique(x[endcap])
    r = rs[ri] * np.ones(len(u))
    plt.plot(r, u, '.', markersize='1')

plt.title('Equilibrium of\n$x_{n + 1} = rx_{n}(1 - x_{n})$', fontsize=20)
plt.xlabel('Value of "r"', fontsize=15)
plt.ylabel('$Limit_{n → ∞}$ {$x_{n}$}', fontsize=15) 
plt.show()