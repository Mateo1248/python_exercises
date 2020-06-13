'''
####################################################
Odpowiedz
####################################################
Inaczej ten dodatkowy parametr można nazwać biasem lub progiem pobudzenia, służy on do dostosowania
mocy wyjściowej wraz z ważoną sumą danych wejściowych do neuronu, dotego za jedo pomocą możemy przesuwać 
funkcję aktywacji w lewo lub prawo.
'''

import sys
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
            output_error = self.error(Y, predicted[-1])
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
    def error(actual, predicted):
        return actual-predicted




IN = np.array(
    [
        [0,0,1],
        [1,0,1],
        [0,1,1],
        [1,1,1]
    ]
)

XOR = np.array(
    [
        [0,1,1,0]
    ]
).T

AND = np.array(
    [
        [0,0,0,1]
    ]
).T

OR = np.array(
    [
        [0,1,1,1]
    ]
).T

input_loop = True
print("####################################################################################")
print("To start training type model from [or, and, xor], n as number od training repeat.")
print("Use ctrl+c to  quit.")
print("####################################################################################")

while True:

    nn = {}
    nn["sig sig"] = NeuralNetwork([3,4,1], [Sigmoid, Sigmoid])
    nn["relu sig"] = NeuralNetwork([3,4,1], [Relu, Sigmoid])
    nn["sig relu"] = NeuralNetwork([3,4,1], [Sigmoid, Relu])
    nn["relu relu"] = NeuralNetwork([3,4,1], [Relu, Relu])

    while input_loop:
        try: 
            OUT = eval(input("model:").upper())
            TRAINING_LOOP = int(input("n:"))
            input_loop = False
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            print("Something went wrong, try one more time!")

    input_loop = True

    for _ in range(TRAINING_LOOP):
        for el in nn:
            nn[el].training(IN, OUT)

    for el in nn:
        print("\n#####################################")
        print(el)
        predicted = nn[el].predict(IN)[2]
        print(f"{'{:8}'.format('tr_input')} \t {'{:8}'.format('tr_output')} \t {'{:8}'.format('predicted')} \t {'{:8}'.format('error')} \t ")
        for i in range(len(predicted)):
            print(f"{IN[i]} \t {'{:+.8f}'.format(OUT[i][0])} \t {'{:+.8f}'.format(predicted[i][0])} \t {'{:+.8f}'.format((predicted[i]-OUT[i])[0])}")
    print("\n")