# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 23:10:49 2017

@author: a550859
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from sklearn import tree
csv=pd.read_csv('C:/Users/a550859/Desktop/py training/Sampledata/job.csv')
columns="ODATE MEMNAME DIFF".split()
df=pd.DataFrame(csv,columns=columns)
y=csv.MEMNAME
X_train,X_test,y_train,y_test=sklearn.cross_validation.train_test_split(df,y,test_size=0.2)
print(X_train.shape)
model=tree.DecisionTreeRegressor()
model.fit(X_train,y_train)
model.score(X_train,y_train)
predicted=model.predict(X_test)


