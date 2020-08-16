# This program demonstrates various properties and applications of quaternions.

import numpy
from pyquaternion import Quaternion

my_quaternion = Quaternion(1, 2, 3, 4)
my_inverse = my_quaternion.inverse

numpy.set_printoptions(suppress=True) # Suppress insignificant values for clarity
v = numpy.array([0, 0, -1]) # Unit vector in the -z direction
v_prime = my_quaternion.rotate(v)
v_undo = my_inverse.rotate(v_prime)

print(v_prime)
print(v_undo)
print(v_prime - v_undo)
