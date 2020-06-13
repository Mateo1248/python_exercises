from animation import *


nn_animation(
    lambda x: np.sin(x), #aproximation function
    [-5,10], #xrange
    [-1,1], #yrange
    [1,20,1], #model shape
    [Sigmoid, Tanh], #activation functions
    step=100,
    accuracy=10,
    interval=100
)