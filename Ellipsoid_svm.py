'''
__author__: Jiaming Shen
__description__: IE521 HW3: Implement the elliposid method for soft-SVM
'''

import numpy as np
import scipy as sp

def read_in_data(inputFileName):
    X = []
    y = []
    with open(inputFileName,"r") as fin:
        for line in fin:
            line = line.strip()
            if line:
                segs = line.split(",")
                X.append([float(feature) for feature in segs[2:]])
                if segs[1] == "M": # "M" means positive example
                    y.append(1.0)
                else: # "B" means negative example
                    y.append(-1.0)
        X = np.array(X)
        y = np.array(y)
        
        (m, n) = X.shape
        y = y.reshape(m,1)
        
    return (X,y)

def zero_order_oracle(X, y, w_combined, lambd):
    (m,n) = X.shape
    w = w_combined[:-1,0].reshape([n,1])
    b = w_combined[-1,0]
    
    f = (1.0/m) * sum(np.maximum( 1 - y * ( np.dot(X,w) + b ), 0))
    f = f + ( lambd * np.dot(w.T, w) )
    return f

def first_order_oracle(X, y, w_combined, lambd):
    (m,n) = X.shape
    w = w_combined[:-1,0].reshape([n,1])
    b = w_combined[-1,0]
    
    tmp = y*(np.dot(X,w) + b)
    ind = np.where(tmp < 1)[0] # the index of examples that y_i*(w^T * x_i + b) < 1
    dw = (1.0/m) * np.sum( (-1.0 * y[ind]*X[ind]), axis=0)
    dw = dw.reshape([n,1])
    dw = dw + 2*lambd*w
    
    db = (1.0/m) * np.sum( -1.0 * y[ind] )
    
    d = np.vstack((dw,db))
    
    return d

def ellipsoid(X,y,lambd, track_flag = False):
    (m,n) = X.shape
    n = n + 1 # add one dimension for b
    R = 1.0 / np.sqrt(lambd)
    c = np.zeros([n,1]) # c = [w,b]^T
    Q = (R**2) * np.eye(n)

    p_star = 1e10 # optimal value
    c_star = None # optimal solution
    T = 100 # iteration number

    if track_flag:
        logs = []

    for t in range(T):
        w = first_order_oracle(X, y, c, lambd)
        c_new = c - (1.0/(n+1)) * np.dot(Q,w) / (np.sqrt( np.dot(np.dot(w.T, Q),w) ) )
        tmp = (np.dot(np.dot(np.dot(Q, w), w.T), Q)) / (np.dot(np.dot(w.T, Q), w))
        Q_new = (1.0*(n**2)/(n**2-1)) * ( Q - (2.0/(n+1)) * tmp )

        c = c_new
        Q = Q_new

        p_cur = zero_order_oracle(X, y, c, lambd)
        if(p_cur < p_star ):
            p_star = p_cur
            c_star = c

        if(track_flag):
            logs.append([t, p_cur[0][0], p_star[0][0]])

    
    if(track_flag):
        return (c_star, p_star, logs)
    else:
        return (c_star, p_star)

def misclassified_rate(X,y,c_star):
    (m,n) = X.shape
    w_star = c_star[:-1,0].reshape([n,1])
    tmp = y*np.dot(X,w_star)
    wrong_number = len(np.where(tmp < 1)[0])
    
    rate = 1.0 * wrong_number / m
    return rate


if __name__ == '__main__':
    inputFileName = "./wdbc.txt"
    (X,y) = read_in_data(inputFileName)
    lambd = 1.0
    # (c_star, p_star) = ellipsoid(X, y, lambd, track_flag=False)
    # print(c_star, p_star)

    (c_star, p_star, logs) = ellipsoid(X, y, lambd, track_flag=True)
    # outputFileName = "./data_to_plot.txt"
    # with open(outputFileName,"w") as fout:
    #     for ele in logs:
    #         fout.write(str(ele[0])+"\t"+str(ele[1])+"\t"+str(ele[2])+"\n")

    rate = misclassified_rate(X,y,c_star)
    print("Number classification rate = %s" % rate)

