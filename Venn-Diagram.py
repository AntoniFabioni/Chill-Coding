'''
This program helps visualize data with multiple characteristics.
The data will be displayed in the form a Venn Diagram
'''

import matplotlib.pyplot as plt
from venn import venn

animals = {
    "Lives on Land": {"Turle", "Llama", "Zebu", "Frog", "Mudskipper", "Hookie"},
    "Swims Underwater": {"Abba Abba", "Salmon", "Sea Snail", "Flying Fish", "Frog", "Hookie", "Mudskipper"},
    "Flys in the Sky": {"Ladybug", "Flying Fish", "Butterfly", "Falcon", "Hookie"}
}
venn(animals)
plt.show()