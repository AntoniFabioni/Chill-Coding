from math import *

# def juggler(n):
#     if n == 1:
#         return 1

#     if n % 2 == 0:
#         juggler(math.floor(math.sqrt(n)))
#     else:
#         juggler(math.floor(math.sqrt(n)**3))
    
#     print(juggler(3))

def printJuggler(n):

    a = n
    print(a)
  
    while a != 1: 

        b = 0
  
        if a % 2 == 0: 

            b  = floor(sqrt(a))
  
        else:
  
            b = floor(sqrt(a)*sqrt(a)*sqrt(a))

        print(b)
        a = b

printJuggler(3)