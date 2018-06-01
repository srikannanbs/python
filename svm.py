# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:19:45 2017

@author: a550859
"""

import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
dataset = pd.read_csv("C:/Users/a550859/Documents/R/Workfolder/SN_IM.csv")
dataset.head(5)