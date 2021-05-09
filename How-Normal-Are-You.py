'''
This program finds similarities between people's interests.
This is done by computing how many people are "related"
by N links (e.g., subbed to the same N YouTube channels).
'''

import numpy as np
import matplotlib as plot

people = {
    'me': {1,2,3},
    'person1': {2,3,4},
    'person2': {1,2,5},
    'person3': {0}
}

def ShowSimilarities(dict, reference):

    for key in dict:
    
        if key == reference:
            continue

        print(key, ':',len(dict[key].intersection(dict[reference])), '->', dict[key].intersection(dict[reference]))

ShowSimilarities(people, 'me')