'''
This program finds similarities between people's interests.
This is done by computing how many people are subscribed to at least
"N" YouTube channels (or something similar).
'''

import numpy as np
import matplotlib as plot

user = {}
others = {}

# ---------------------