# -*- coding: utf-8 -*-
"""
Created on Tue Oct 09 13:49:07 2018

@author: harshal
"""

import numpy as np
import os

#normalization function
def normalize(Mat):
    row_sums = Mat.sum(axis=1)
    newMat = Mat/row_sums[:,np.newaxis]
    return newMat
    
def print_directory_contents(sPath):
    for schild in os.listdir(sPath):
        schildpath = os.path.join(sPath,schild)
        if os.path.isdir(schildpath):
            print_directory_contents(schildpath)
        else:
            print(schildpath)
            
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 

f(2)
f(3,[3,2,1])
f(3)           
                
        
# set seed
np.random.seed(0)
random.seed(3)

# initialize a matrix of given dimension
dim = 3
Mat = 2*np.ones((dim,dim))
NMat = normalize(Mat)

#print directories and files (recursion example)
#sPath = os.getcwd()
#print_directory_contents(sPath)

#A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
#A1 = range(10)
#A2 = sorted([i for i in A1 if i in A0])
#A3 = sorted([A0[s] for s in A0])
#A4 = [i for i in A1 if i in A3]
#A5 = {i:i*i for i in A1}
#A6 = [[i,i*i] for i in A1]

