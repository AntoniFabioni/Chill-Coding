from random import randint
import matplotlib.pyplot as plt

def BrokenClock(tLimit, Count, Percent):

    Clock, t = 0, 0

    while t < tLimit and Clock < Count:
        Clock += 1
        t += 1
        RNG = randint(1, 100)

        if RNG <= Percent and Clock < Count:
            ErrorBit = 1 << randint(0, 3)
            Clock ^= ErrorBit

    return t

def BrokenPlot(Iterations):
    
    Ys = []

    for i in range(101):

        y_i = 0
        for n in range(Iterations):
            y_i += 1000 * BrokenClock(100, 15, i) / Iterations
        y_i /= 1000

        Ys.append(y_i)

    plt.plot(Ys)
    plt.show()

BrokenPlot(1000)