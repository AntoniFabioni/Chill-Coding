'''
Creating a neural network from scratch that predicts the
output of a boolean function given sample inputs.
'''

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_input = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])

training_output = np.array([[0,1,1,1]]).T

np.random.seed(1)

weights = 2 * np.random.random((3,1)) - 1

print("Random starting weights are:")
print(weights)

for i in range(1):
    input_layer = training_input
    output_layer = sigmoid(np.dot(input_layer, weights))

print("Outputs are:")
print(output_layer)
