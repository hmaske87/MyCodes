# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 17:39:45 2018

@author: hmaske2
"""
import numpy as np

def gradDesc(x0, alpha):
    eps = 0.001
    Niter = 100
    x_0 = x0
    k=1
    t=10
    while t > eps and k < Niter:
        x_n = x_0 - alpha*2*x_0
        x_0 = x_n
        t = np.abs(2*x_0)
        k = k + 1
    return x_n, k, t

x0=4
alpha=0.1
minValue,k,t = gradDesc(x0,alpha)

        
        