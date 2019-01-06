# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 19:07:05 2019

@author: harshal
"""

# k-means algorithm
import numpy as np
import matplotlib.pyplot as plt

def kmeans(X,k):
    


# generate 2-D gaussian data
mu = np.zeros((3,2))
mu = [[1,2],[2,4],[5,5]]
X = np.zeros((30,2))
L=10
sig=0.1*np.eye(2)
for j in range(len(mu)):
    for i in range(L):
        X[i+L*(j-1),:] = np.random.normal(mu[j][:],[0.4,0.2])
        

plt.plot(X[:,0],X[:,1],'+')
plt.show()
        
        