#!/usr/bin/python

import numpy as np

scores =np.array([3.0, 1.0, 0.2])

def softmax(x):
    res=np.exp(x)
    nres=res/np.sum(res,axis=0) #Axis 0 is here for strange reasons
    return nres
"""Compute softmax values for each sets of scores in x."""
# TODO: Compute and return softmax(x)

print(softmax(scores/10))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1) #just a vector made of floats from -2.0->6 with 0.1 increments
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
plt.plot(x, softmax(scores).T, linewidth=2)
#plt.show()



"""
Problem description:

You have a classifier that outputs 3 scores, operating over N samples.
Design a softmax function that takes a 3xN array as input, and returns
a 3xN array as output.

"""
