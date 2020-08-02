import numpy
from pyquaternion import Quaternion

my_quaternion = Quaternion(axis=[1, 0, 0], angle=3.14159265)
my_inverse = my_quaternion.inverse

numpy.set_printoptions(suppress=True) # Suppress insignificant values for clarity
v = numpy.array([0., 0., 1.]) # Unit vector in the +z direction
v_prime = my_quaternion.rotate(v)
v_i = my_inverse.rotate(v)

print(v_prime)
print(v_i)