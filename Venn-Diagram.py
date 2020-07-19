'''
This program helps visualize data with multiple characteristics.
An example would be multiple choice survey answers.
The data will be displayed in the form a Venn Diagram
'''

import matplotlib.pyplot as plt
from venn import venn

numbers = {
    "A": {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16},
    "B": {0, 2, 4, 6, 8, 10, 12, 14, 16},
    "C": {0, 3, 6, 9, 12, 15},
    "D": {0, 4, 8, 12, 16},
    "E": {0, 5, 10, 15}

}

venn(numbers, fmt="{percentage:.1f}%", fontsize=8, legend_loc="upper right")

plt.show()
