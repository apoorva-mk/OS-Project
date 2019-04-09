# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:01:19 2019

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
    proc = [i for i in range(1,10)]
    a =    findavgTime_rr(proc,n,X_train[i],2)
    b = findavgTime_fcfs(proc, n, X_train[i]) 
    if(a<b):
        Y_train[i] ="rr"
    else:
        Y_train[i] = "fcfs"
        
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
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
    proc = [i for i in range(1,10)]
    
    a =    findavgTime_rr(proc,n,X_test[i],2)
    b = findavgTime_fcfs(proc, n, X_test[i]) 
    
    if(a<b):
        Y_test[i] ="rr"
    else:
        Y_test[i] = "fcfs"


y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)

cm

from sklearn.metrics import accuracy_score, precision_score,recall_score,matthews_corrcoef,cohen_kappa_score

print("Accuracy:"+str(accuracy_score(Y_test,y_pred)))


cm
