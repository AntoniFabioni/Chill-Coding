'''
This program has the goal of creating a perceptron
that accepts non-training inputs.
'''

import numpy as np

class NeutralNet():

    def __init__(self):
        self.weights = 2 * np.random.random((3, 1)) - 1
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return np.exp(-x) / (1 + np.exp(-x))**2

    def train(self, training_inputs, training_outputs, training_iterations):
        for i in range(training_iterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.weights += adjustments
    
    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.weights))
        return output
    
if __name__ == "__main__":
    
    neural_net = NeutralNet()
    
    print("Random starting weights are:")
    print(neural_net.weights)
    print("\n")

    training_input = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])

    training_output = np.array([[0,1,1,0]]).T

    neural_net.train(training_input, training_output, 10000)

    print("Weights after training are:")
    print(neural_net.weights)
    print("\n")

    X = str(input("Input 1: "))
    Y = str(input("Input 2: "))
    Z = str(input("Input 3: "))

    print("New data = ", X, Y, Z)
    print("New output = ", neural_net.think(np.array([X, Y, Z])))