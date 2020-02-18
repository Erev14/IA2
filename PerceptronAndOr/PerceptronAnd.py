"""
Created on Mon Feb 17 07:47:28 2020

@author: Erev14
"""
# import paqueteria
import numpy as np
from perceptron import perceptron

# create input entries x1, x2
inp = np.ones((4,2), dtype="int32")
inp[0:-1:2,-1] = 0
inp[0:2,0]=0
# inp = np.array([[0,0],[0,1],[1,0], [1,1]])

#create output entries AND -> y
out = np.zeros((4,1), dtype="int32")
out[-1,-1] = 1
# out = np.array([[0],[0],[0], [1]])

# create weight matrix for calculation
weight = 1
weights = np.concatenate( ( np.full((inp.shape), weight) , np.ones((4,1)) ), axis=1 )

# check if the perceptron gets the same output
res = perceptron(inp, out, weights, threshold = 1.5)
print(res)
