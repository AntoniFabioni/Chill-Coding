'''
This program finds similarities between people's interests.
This is done by computing how many people are "related"
by N links (e.g., subbed to the same N YouTube channels).
'''

import numpy as np
import matplotlib as plot

me = {1,2,3}
them = {2,3,4}

intersection = me.intersection(them)

print(intersection)