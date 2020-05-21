import numpy as np
import random
import math


#transition functions
class Sigmoid:
    f = lambda x: 1./(1. + np.exp(-x))
    fd = lambda x: x*(1.-x)


class Relu:
    f = lambda x : x*(x>0)
    fd = lambda  x : 1.*(x>0) 


class Tanh:
    f = lambda x : np.tanh(x)
    fd = lambda  x : 1.0 - np.tanh(x)**2


class NeuralNetwork:
    
    weights: list
    activation_functions: list
    layers: int 
    learning_coeficient: float 


    def __init__(self, shape: list, activation_functions: list, learning_coeficient = 5e-1):
        self.weights = []
        self.layers = len(shape)-1
        for i in range(self.layers):
            self.weights.append(2*np.random.rand(shape[i], shape[i+1])-1)
        self.activation_functions = activation_functions
        self.learning_coeficient = learning_coeficient


    def predict(self, input: np.array):
        outputs = []
        outputs.append(input) 
        for l in range(self.layers):
            w = self.weights[l]
            f = self.activation_functions[l].f
            outputs.append( f(np.dot(outputs[-1], w)) )
        return outputs


    def training(self, X: np.array, Y: np.array):

            #back propagation
            #make prediction
            predicted = self.predict(X)
            
            #get output activation function
            fd = self.activation_functions[-1].fd
            
            #count output error and delta
            delta = []
            output_error = self.__error_der(Y, predicted[-1])
            delta.insert(0, output_error * fd(predicted[-1]))

            #propagate error on the rest of the layers
            for i in range(self.layers-2, -1, -1):
                fd = self.activation_functions[i].fd
                medium_error = np.dot(delta[0], self.weights[i+1].T)
                delta.insert(0, medium_error * fd(predicted[i+1]))

            #update weights

            for i in range(self.layers):
                self.weights[i] += self.learning_coeficient * np.dot(predicted[i].T, delta[i])
    

    @staticmethod
    def __error_der(actual, predicted):
        return actual-predicted
