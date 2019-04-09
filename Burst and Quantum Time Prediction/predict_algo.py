# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:55:46 2019

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
        
        


Y_train = [ None for i in range(1000)]

for i in range(1000):
    n=10
    proc = [j for j in range(1,10)]
    a =    findavgTime_rr(proc,n,X_train[i],2)
    b = findavgTime_fcfs(proc, n, X_train[i])
    d_sjf = [ None for j in range(10)]
    for k in range(10):
        d_sjf[k] = [ None for j in range(3)]
    for j in range(10):
        d_sjf[j][0]=i+1
        d_sjf[j][1]=X_test[i][j]
        d_sjf[j][2]=10
    c=findavgTime_sjf(d_sjf,n)
    if(a<b and a<c):
        Y_train[i] ="rr"
    elif(b<c):
        Y_train[i] = "fcfs"
    else:
        Y_train[i]="sjf"



        
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, Y_train)


X_test = [ None for i in range(1000)]
for i in range(1000):
    X_test[i]=[ None for j in range(10)]


for i in range(1000):
    for j in range(10):
        X_test[i][j] = random.randrange(1,100)
        
        


Y_test = [ None for i in range(1000)]

for i in range(1000):
    n=10
    proc = [j for j in range(1,10)]
    a =    findavgTime_rr(proc,n,X_test[i],2)
    b = findavgTime_fcfs(proc, n, X_test[i]) 
    
    d_sjf = [ None for j in range(10)]
    for k in range(10):
        d_sjf[k] = [ None for j in range(3)]
    for j in range(10):
        d_sjf[j][0]=j+1
        d_sjf[j][1]=X_test[i][j]
        d_sjf[j][2]=10
    c=findavgTime_sjf(d_sjf,n)
    if(a<b and a<c):
        Y_test[i] ="rr"
    elif(b<c):
        Y_test[i] = "fcfs"
    else:
        Y_test[i]="sjf"
    
    

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)

cm

from sklearn.metrics import accuracy_score, precision_score,recall_score,matthews_corrcoef,cohen_kappa_score

print("Accuracy:"+str(accuracy_score(Y_test,y_pred)))

cm

X_ans =[ [ None for i in range(10)]]
for i in range(10):
    li =[ [ None for j in range(9)]]
    for j in range(9):
        li[0][j] = random.randrange(0,10)
    temp=predic_burst(li)
    X_ans[0][i] = temp[0]
    
    
        

y_ans = classifier.predict(X_ans)


