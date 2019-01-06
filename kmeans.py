# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 19:07:05 2019

@author: harshal
"""

# k-means algorithm
import numpy as np
import matplotlib.pyplot as plt

def kmeans(X,k):
#    initialize the means from global mean and variance
    Xmean = np.mean(X,axis=0)
    Xvar = np.var(X,axis=0)
    d = Xmean.size
    muInit=np.zeros((3,d))
    for y in range(k):
#        muInit[y,:] = np.random.normal(Xmean,Xvar,size=2)
        for z in range(d):
            muInit[y,z] = np.random.uniform()*max(X[:,z])/1.5
#    Declare temporary variables needed: dimension, data length, assignment, termination condition
    L = X.shape[0]
    zAssign = [1]*L
    eps=0.1
    Miter=30
    dDiff = 1
    m=1
    
    while dDiff>eps and m<Miter:
        dDiff = 0
#Compute distance of each point from the cluster means and assign to the closest mean
        for i in range(L):
            Dist=[]
            for j in range(k):
                Dist.append(np.linalg.norm(X[i,:]-muInit[j,:]))
            temp = zAssign[i]
            zAssign[i] = Dist.index(min(Dist))
            if zAssign[i] != temp:
                dDiff += 1
        print('looped %d times'%m + 'with Difference %d ' % dDiff)
        m+=1
# Update the cluster means
        Dist=[]
        for j in range(k):
            for i in range(L):
                if zAssign[i]==j:
                    Dist.append(X[i,:])
            if len(Dist)>0:
                muInit[j,:]=np.mean(Dist,axis=0)
    return zAssign, muInit

# generate 2-D gaussian data
mu = np.zeros((3,2))
mu = [[1,2],[2,4],[5,5]]
X = np.zeros((30,2))
L=10

for j in range(len(mu)):
    for i in range(L):
        X[i+L*(j-1),:] = np.random.normal(mu[j][:],[0.4,0.2])

plt.plot(X[:,0],X[:,1],'+')
plt.show()
z, d2mean = kmeans(X,3)
print(z)

mu=[-1,5,10]
X = np.zeros((30,1))
for j in range(len(mu)):
    for i in range(L):
        X[i+L*(j-1),:] = np.random.normal(mu[j],0.01)
z, d1mean = kmeans(X,3)
print(z)
#plt.plot(X[:,0],X[:,1],'+')
#plt.show()
