'''
This program helps visualize data with multiple characteristics.
The data will be displayed in the form a Venn Diagram
'''

import matplotlib.pyplot as plt
from venn import venn

numbers = {
    "A": {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15},
    "B": {0, 2, 4, 6, 8, 10, 12, 14},
    "C": {0, 3, 6, 9, 12, 15},
    "D": {0, 4, 8, 12}

}

venn(numbers, fmt="{percentage:.1f}%", fontsize=10, legend_loc="upper right")

plt.show()