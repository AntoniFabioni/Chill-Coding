# This program is under construction.

def f(x):
    
    return x * (1 - x)

def iterate(start, n, r):

    ans = start

    for i in range(n):

        ans = r * f(ans)

    return ans


print(iterate(0.5, 10, 0))
print(iterate(0.5, 10, 0.5))
print(iterate(0.5, 10, 1))
print(iterate(0.5, 10, 1.5))
print(iterate(0.5, 10, 2))
print(iterate(0.5, 10, 2.5))
print(iterate(0.5, 10, 3))
print(iterate(0.5, 10, 3.1))
print(iterate(0.5, 10, 3.2))
print(iterate(0.5, 10, 3.3))