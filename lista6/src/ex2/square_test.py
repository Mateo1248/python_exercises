from animation import *

nn_animation(
    lambda x: x**2, #aproximation function
    [-50,50], #xrange
    [0,50**2], #yrange
    [1,10,1], #model shape
    [Relu, Sigmoid], #model activation functions
    step=5,
    accuracy=1
)