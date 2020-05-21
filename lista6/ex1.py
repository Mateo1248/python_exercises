'''
####################################################
Odpowiedz
####################################################
Inaczej ten dodatkowy parametr można nazwać biasem lub progiem pobudzeniasłuży on do dostosowania
mocy wyjściowej wraz z ważoną sumą danych wejściowych do neuronu, dotego za jedo pomocą możemy przsuwać 
funkcję aktywacji w lewo lub prawo.
'''

from neural_network import *
import sys

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