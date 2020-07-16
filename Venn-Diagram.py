'''
This program helps visualize data with multiple characteristics.
The data will be displayed in the form a Venn Diagram
'''

import matplotlib.pyplot as plt
from venn import venn

animals = {
    "Lives on Land": {"Turle", "Llama", "Zebu", "Frog", "Mudskipper", "Hookie", "Otter", "Snake", "Snail", "Dragon"},
    "Digs Underground": {"Mole", "Mole Cricket", "Cicada", "Snake", "Snail", "Dragon"},
    "Swims Underwater": {"Abba Abba", "Salmon", "Sea Snail", "Flying Fish", "Frog", "Hookie", "Mudskipper", "Snail", "Dragon"},
    "Flies in the Sky": {"Ladybug", "Flying Fish", "Butterfly", "Falcon", "Hookie", "Otter", "Cicada", "Dragon"}

}

venn(animals, fmt="{percentage:.1f}%", fontsize=10, legend_loc="upper right")

plt.show()