# -*- coding: utf-8 -*-
"""
Created on Sun Jan 06 19:03:46 2019

@author: hmaske2
"""

import numpy as np
import scipy as sp

def read_in_data(inputFileName):
    X = []
    y = []
    with open(inputFileName,'r') as fin:
        for line in fin:
            line = line.strip()
            if line:
                segs=line.split(",")
                X.append([float(feature) for feature in segs[2:]])
                if segs[1]=='M':
                    y.append(1.0)
                else:
                    y.append(-1.0)
        X = np.array(X)
        y = np.array(y)
        
        (m,n) = X.shape
        y = y.reshape(m,1)
    return (X,y)
                    
                


if __name__=='__main__':
    inputFileName = './wdbc.txt'
    (X,y) = read_in_data(inputFileName)