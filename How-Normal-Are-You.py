'''
This program finds similarities between people's interests.
This is done by computing how many people are "related"
by N links (e.g., subbed to the same N YouTube channels).
'''

import numpy as np
import matplotlib as plot

user = {}
others = {}

# -------------------------