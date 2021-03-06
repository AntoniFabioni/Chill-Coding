# This program demonstrates various properties and applications of quaternions.

import numpy
from pyquaternion import Quaternion

my_quaternion = Quaternion(1, -2, 3, -4)
my_inverse = my_quaternion.inverse

numpy.set_printoptions(suppress=True) # Suppress insignificant values for clarity
u = numpy.array([0, -3/5, 4/5]) # Unit vector
v = numpy.array([0, 3/5, -4/5]) # Unit vector

u_prime = my_quaternion.rotate(u)
u_undo = my_inverse.rotate(u_prime)
v_prime = my_quaternion.rotate(v)
v_undo = my_inverse.rotate(v_prime)


print(v_prime)
print(v_undo)
print(u_prime)
print(u_undo)
