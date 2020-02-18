from matplotlib import pyplot as plt
import numpy as np

def perceptron(x, y, weights, threshold, activation_fun = 1):
        # x with expected outputs
        xo = np.concatenate( (x, y), axis=1 )
        print("x with expected outputs")
        print(xo)
        # x multiply by weights
        xw = xo * weights # v = x.dot(weights)
        print(xw)
        # sum from xiwi to xnwn, without the outputs
        sum = np.sum(xw[:,0:-1], axis = 1, keepdims = True)
        print(sum)
        # - theta
        v = sum - threshold
        print(v)
        # calculate the f(v)
        if activation_fun:
            # step function
            fv = np.where(v >= 0, 1, 0)
        return fv

#def graph:
    #a = 0
