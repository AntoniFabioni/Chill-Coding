# This program is under construction.

import matplotlib.pyplot as plt

def f(x):
    
    return x * (1 - x)

def iterate(start, n, r):

    ans = start

    for i in range(n):

        ans = r * f(ans)

    return ans

x = [i / 100000 for i in range(400000)]

y = [iterate(0.5, 10, i) for i in x]

plt.plot(x, y)
plt.show()