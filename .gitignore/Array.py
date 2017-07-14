# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:54:47 2017

@author: a550859
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s=pd.Series([1,np.nan])
print(s)
dates=pd.date_range('20170101',periods=6)
print (dates)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df.index)
print(df.columns)
print (df)
print(df.describe)


df2=pd.DataFrame({'A':1.,
                  'B': pd.Timestamp('20170506'),
                  'C': pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D': np.array([3]*4,dtype='int32'),
                  'E': pd.Categorical(["test","train","test","train"]),
                  'F':'st'})      
print(df2)
print(df2.describe)
print(df.T)
print(df.sort_index(axis=1,ascending='FALSE'))
print(df.sort_values(by='B'))
print(df['C'])
print(df[0:2])
print(df.loc[dates[0]])
df3=df.copy()
print(df3)
df3[df3 > 0]= -df3
print(df3)


df1=df.reindex(index=dates[0:4],columns=list(df.columns)+['E'])
df1.loc[dates[0]:dates[1],'E']=1
print(df1)
df1.dropna(how='any')
print(df1)
df1.fillna(value=5)
pd.isnull(df1)
df.mean()

s=pd.Series([1,2,5,np.nan,4,8],index=dates)
s
df.apply(np.cumsum)
s=pd.Series(np.random.randint(0,7,size=10))
print(s)
s.value_counts()

df=pd.DataFrame(np.random.randn(10,4))
df
s=df[:3]
df5=df.append(s,ignore_index=True)
df5
df1=df5.reindex(index=list(df5.columns),columns=list(df.columns)+['4'])
df1

df=pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
df
s=df.iloc[3]
s
df.append(s,ignore_index=True)

df=pd.DataFrame({'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
                 'B':['one','two','one','three','two','two','one','three'],
                 'C': np.random.randn(8),
                 'D': np.random.randn(8)
                 })
df
df.melt(id_vars=['A','B'])
df.groupby('A','B).sum()



