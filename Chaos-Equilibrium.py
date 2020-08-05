# This program is under construction.

def f(x):
    
    return x * (1 - x)

def iterate(start, n):

    ans = start

    for i in range(n):

        ans = f(ans)

    return ans


print(iterate(0.5, 5))