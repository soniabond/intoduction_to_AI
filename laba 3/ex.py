import numpy as np
import imageLib

nb_inp = 36
nb_h1 = 50
nb_h2 = 50
nb_out = 5

x, y = imageLib.initXAndY()

np.random.seed(1)


def reset():
    w1 = np.random.normal(scale=0.1,size=(nb_inp,nb_h1))
    w2 = np.random.normal(scale=0.1,size=(nb_h1,nb_h2))
    w3 = np.random.normal(scale=0.1,size=(nb_h2,nb_out))
    b1 = np.zeros(nb_h1)
    b2 = np.zeros(nb_h2)
    b3 = np.zeros(nb_out)
    return w1, w2, w3, b1, b2, b3

params = reset()

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_prime(x):
    return x*(1-x)


def train(x, y, w1, w2, w3, b1, b2, b3):
    # feed forward
    inp_l = x
    l1 = sigmoid(np.dot(inp_l, w1) + b1)
    l2 = sigmoid(np.dot(l1, w2) + b2)
    l3 = sigmoid(np.dot(l2, w3) + b3)

    # backpropagation
    delta_l3 = (y - l3) * sigmoid_prime(l3)
    delta_l2 = delta_l3.dot(w3.T) * sigmoid_prime(l2)
    delta_l1 = delta_l2.dot(w2.T) * sigmoid_prime(l1)

    # update weights
    w3 += (np.dot(l2.T, delta_l3))
    w2 += (np.dot(l1.T, delta_l2))
    w1 += (np.dot(inp_l.T, delta_l1))

    #  update biases
    b3 = b3 + (np.sum(delta_l3, axis=0))
    b2 = b2 + (np.sum(delta_l2, axis=0))
    b1 = b1 + (np.sum(delta_l1, axis=0))


    return w1, w2, w3, b1, b2, b3



def predict(x, w1, w2, w3, b1, b2, b3):
    l1 = sigmoid(np.dot(x, w1) + b1)
    l2 = sigmoid(np.dot(l1, w2) + b2)
    l3 = sigmoid(np.dot(l2, w3) + b3)
    return l3


def trainModel(epoch):
    global params
    params = reset()
    for i in range(0,epoch) :
        params = train(x,y,*params)


def makePrediction(path):
    test = imageLib.imageToArray(path)
    global params
    res = predict(test, *params)
    return imageLib.defineLetter(res)