import numpy as np
import random
import math




#transition functions
class Sigmoid:
    @staticmethod
    def f(x):
        return 1/(1 + np.exp(-x))
    

    @staticmethod
    def fd(x):
        return x*(1 - x)




class Relu:
    @staticmethod
    def f(x):
        return x*(x>0)
    

    @staticmethod
    def fd(x):
        return 1*(x>0)




class Tanh:
    @staticmethod
    def f(x):
        return np.tanh(x)
    

    @staticmethod
    def fd(x):
        return 1.0 - np.tanh(x)**2




class NeuralNetwork:
    weights: list
    biases: list
    activation_functions: list
    layers: int 
    learning_coeficient: float 
    

    def __init__(self, shape: list, activation_functions: list, learning_coeficient = 5e-1):
        self.weights = []
        self.biases = []
        self.layers = len(shape)-1
        for i in range(self.layers):
            self.weights.append(2*np.random.rand(shape[i], shape[i+1])-1)
            self.biases.append(np.zeros((1, shape[i+1])))
        self.activation_functions = activation_functions
        self.learning_coeficient = learning_coeficient


    def predict(self, input: np.array):
        outputs = []
        outputs.append(input) 
        for l in range(self.layers):
            w = self.weights[l]
            b = self.biases[l]
            f = self.activation_functions[l].f
            outputs.append( f(np.dot(outputs[-1], w) + b))
        return outputs


    def training(self, X: np.array, Y: np.array):

            predicted = self.predict(X)
            
            delta = []
            delta.insert(0, self.error(predicted[-1], Y))

            for i in range(self.layers-2, -1, -1):
                fd = self.activation_functions[i].fd
                delta.insert(0, np.dot(delta[0], self.weights[i+1].T) * fd(predicted[i+1]))

            for i in range(self.layers):
                self.weights[i] -= self.learning_coeficient * np.dot(predicted[i].T, delta[i])
                self.biases[i] -= self.learning_coeficient * np.sum(delta[i], axis=0)


    @staticmethod
    def error(predicted, actual):
        n_samples = actual.shape[0]
        res = predicted - actual
        return res/n_samples
