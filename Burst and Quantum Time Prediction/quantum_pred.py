# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:33:16 2019

@author: arpit
"""

import numpy as np

import random
X_train = [ None for i in range (1000)]

for i in range(1000):
    X_train[i]=[ None for j in range(10)]


for i in range(1000):
    for j in range(10):
        X_train[i][j] = random.randrange(1,100)

Y_train = [ None for i in range(1000) ]
        
for i in range(1000):
    n=10
    proc = [j for j in range(1,10)]
    ans = 1000000
    for q in range(3,10):
        a =    findavgTime_rr(proc,n,X_train[i],q)
        if(a<ans):
            Y_train[i]=q
            ans = a




X_test = [ None for i in range (1000)]

for i in range(1000):
    X_test[i]=[ None for j in range(10)]


for i in range(1000):
    for j in range(10):
        X_test[i][j] = random.randrange(1,100)

Y_test = [ None for i in range(1000) ]
        
for i in range(1000):
    n=10
    proc = [j for j in range(1,10)]
    ans = 1000000
    for q in range(3,10):
        a =    findavgTime_rr(proc,n,X_test[i],q)
        if(a<ans):
            Y_test[i]=q
            ans = a

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X_train, Y_train)
import math
y_pred=regressor.predict(X_test)
for i in range(1000):
    y_pred[i] = math.floor(y_pred[i])


        
    


