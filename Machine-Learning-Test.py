'''
Creating a very basic perceptron neural network from scratch that
predicts the output of a boolean function given sample inputs.

This exercise is focused on education over nuanced application.
'''

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return np.exp(-x) / (1 + np.exp(-x))**2

training_input = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])

training_output = np.array([[0,1,1,0]]).T

weights = 2 * np.random.random((3,1)) - 1

print("Random starting weights are:")
print(weights)
print("\n")

for i in range(100000):
    input_layer = training_input
    output_layer = sigmoid(np.dot(input_layer, weights))
    error = training_output - output_layer
    adjustments = error*sigmoid_derivative(output_layer)
    weights += np.dot(input_layer.T, adjustments)

print("Weights after training are:")
print(weights)
print("\n")

print("Outputs are:")
print(output_layer)
