# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:48:08 2017

@author: a550859
"""
import pandas as pd
import pandas.util.testing as tm
import numpy as np
tm.N=3
def unpivot(frame):
    N,K=frame.shape
    data={'value':frame.values.ravel('F'),
          'variable':np.asarray(frame.columns).repeat(N),
          'date':np.tile(np.asarray(frame.index),K)}
    return pd.DataFrame(data,columns=['date','variable','value'])
df =unpivot(tm.makeTimeDataFrame())
df

df.pivot(index='date',columns='variable',values='value')
df['value2']=df['value']*2
pivoted=df.pivot('date','variable')
pivoted

columns=pd.MultiIndex.from_tuples([('A','cat'),('B','Dog'),('B','cat'),('A','Dog')],
                                   names=['exp','animal'])
index=pd.MultiIndex.from_product([('bar','baz','foo','qux'),('one','two')],
                                   names=['first','second'])
df=pd.DataFrame(np.random.randn(8,4),index=index,columns=columns)
df

df.stack().mean(1).unstack()
df.stack().groupby(level=0).mean()

values=np.random.randn(10)
values
bins=[0,0.2,0.4,0.6,0.8,1]
pd.get_dummies(pd.cut(values,bins))
s=pd.Series(list('abcaa'))
s
pd.get_dummies(s)

rng = pd.date_range('1/1/2015',periods=24,freq='H')
rng
ts=pd.Series(np.random.randn(len(rng)),index=rng)
ts.head()
converted=ts.asfreq('45Min',method='pad')
converted.head()
ts.resample('D').mean()

periods=[pd.Period('2012-01'),pd.Period('2012-02'),pd.Period('2012-03')]
periods
ts=pd.Series(np.random.randn(3),periods)
ts
type(ts.index)

pd.to_datetime(['2005/11/23'])
