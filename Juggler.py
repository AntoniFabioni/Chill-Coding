import numpy as np

juggles = 0

def juggler(n):
    global juggles
    if n == 1:
        return juggles
    if n % 2 == 0:
        juggles += 1
        juggler(np.floor(np.sqrt(n)))
    else:
        juggles += 1
        juggler(np.floor(np.sqrt(n)**3))

def printJuggler(n):

    a = n
    print(a)
  
    while a != 1: 

        b = 0
  
        if a % 2 == 0: 

            b  = np.floor(np.sqrt(a))
  
        else:
  
            b = np.floor(np.sqrt(a)**3)

        print(b)
        a = b

printJuggler(3)
print(juggler(3))