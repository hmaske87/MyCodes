# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:09:58 2019

@author: harshal
"""

mainStr = 'pqrsxytprqmjklqprsxypqrsd'

tar = 'pqr'

'''find the start index of all permutations of target string'''

L = len(mainStr)
X=[]
for i in range(len(mainStr)):
    temp = list(tar)
    if mainStr[i] in tar:
        while temp and i<L-2:
            temp.remove(mainStr[i])
            i += 1
            if mainStr[i] not in temp:
                break
        if not temp:
            X.append(i)
            