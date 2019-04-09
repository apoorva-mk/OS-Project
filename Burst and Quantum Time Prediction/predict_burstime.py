# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:38:06 2019

@author: arpit
"""

import sklearn 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn import linear_model


def predic_burst(lis):
 #lis is the list of list 
 #load dataset
 process_dataset = pd.read_csv('process_data.csv')

#selecting columns from dataset

#Extracting run time (target values)
 run_time = process_dataset[['RunTime']]

#selecting of process feautures without historical information
 features = process_dataset[['SubmitTime',
                            'UsedMemory',
                            'ReqNProcs',
                            'ReqTime',
                            'ReqMemory',
                            'UserID',
                            'GroupID',
                            'QueueID',
                            'OrigSiteID']]

 label_encoder = preprocessing.LabelEncoder()
 le_features = features.apply(label_encoder.fit_transform)

 X_train, X_test, y_train, y_test = train_test_split( le_features, run_time, test_size=0.20, random_state=42)

 knn = KNeighborsClassifier(n_neighbors= 13)
 knn.fit(X_train, y_train)


 pred = knn.predict(lis)
 return pred



a = predic_burst([ [ 1,1190,0,30,0,27,1,0,0 ] ])
print(a)
