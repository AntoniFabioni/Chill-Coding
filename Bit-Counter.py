from random import randint
import numpy as np
import matplotlib.pyplot as plt

def BrokenClock(tLimit, Count, Percent):

    Clock, t = 0, 0

    while t < tLimit and Clock < Count:
        Clock += 1
        t += 1
        RNG = randint(1, 1000)/10

        if RNG <= Percent and Clock < Count:
            ErrorBit = 1 << randint(0, 3)
            Clock ^= ErrorBit

    return t

def BrokenPlot(Iterations, Resolution):
    
    Ys = []
    Xs = np.linspace(0, 100, Resolution)

    for i in Xs:

        y_i = 0
        for n in range(Iterations):
            y_i += BrokenClock(100, 15, i)
        y_i /= Iterations

        Ys.append(y_i)

    plt.plot(Xs, Ys, color="cornflowerblue")
    plt.title("Expected Time to Reach 1111")
    plt.xlabel("Probability of bit flip (%)")
    plt.ylabel("Time")
    plt.show()

BrokenPlot(20000, 1000)