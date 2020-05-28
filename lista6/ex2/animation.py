import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from neural_network import *
import math
import sys




def nn_animation(f, x_range, y_range, shape, activation, step=10, accuracy=2, interval=100):
    x = np.array([np.linspace(x_range[0], x_range[1], (x_range[1]-x_range[0])*accuracy )]).T
    y = f(x)

    x_norm = x/x_range[1]
    y_norm = y/y_range[1]

    model = NeuralNetwork(shape, activation)

    fig, [ax1, ax2] = plt.subplots(ncols=2)
    
    ax1.plot(x,y)


    def animate(i):

        for _ in range(step):
            model.training(x_norm, y_norm)
        
        loops = step*i

        y_predicted = model.predict(x_norm)[-1]*y_range[1]        
        
        ax2.clear()
        ax2.scatter(x, y_predicted)
        plt.title(f"loops: {loops}")


    anim = FuncAnimation(fig, animate, interval=interval)

    plt.show()

