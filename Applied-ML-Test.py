'''
This program has the goal of creating a perceptron that
evaluates non-training inputs trained on the boolean function:

f([x1, x2, x3, x4, x5]) = ((x1 AND (x2 OR (NOT x3))) XOR ((NOT x1) AND (NOT x4))) OR x5
'''

import numpy as np

training_input = [[0,0,1,0,0],[1,1,1,0,1],[1,0,1,1,1],[0,1,1,1,0],[0,1,1,0,0],[0,1,0,1,0],[1,1,1,1,1]]
training_output = [1,1,1,0,1,0,1]

class NeutralNet():

    def __init__(self):
        #   Randomize weights
        self.weights = 2 * np.random.random((len(training_input[0]), 1)) - 1
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return np.exp(-x) / (1 + np.exp(-x))**2

    def train(self, training_inputs, training_outputs, training_iterations):
        for i in range(training_iterations):
            
            #   Compute output using training inputs
            output = self.think(training_inputs)

            #   Error is difference between actual and expected outputs
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

    training_input = np.array(training_input)

    training_output = np.array([training_output]).T

    neural_net.train(training_input, training_output, 100000)

    print("Weights after training are:")
    print(neural_net.weights)
    print("\n")

    #   Enter test input
    V = str(input("Input 1: "))
    W = str(input("Input 2: "))
    X = str(input("Input 3: "))
    Y = str(input("Input 4: "))
    Z = str(input("Input 5: "))

    #   Compute test output
    print("\n")
    print("New data = ", V, W, X, Y, Z)
    print("New output = ", neural_net.think(np.array([V, W, X, Y, Z])))