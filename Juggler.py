'''
This program prints the juggler sequence starting at an integer "n"
and counts how many steps are needed to return 1.
'''

import numpy as np

juggles = 0

def juggler(n):

    global juggles
    
    if n == 1:
    
        return juggles
    
    if n % 2 == 0:
    
        juggles += 1
        return juggler(np.floor(np.sqrt(n)))
    
    else:
    
        juggles += 1
        return juggler(np.floor(np.sqrt(n)**3))

def printJuggler(n):

    a = n
    print(a)
  
    while a != 1: 

        b = 0
  
        if a % 2 == 0: 

            b  = np.floor(np.sqrt(a))
  
        else:
  
            b = np.floor(np.sqrt(a)**3)

        print(int(b))
        a = b

def Juggle(n):
    printJuggler(n)
    print("Steps taken: ", juggler(n))

Juggle(157)