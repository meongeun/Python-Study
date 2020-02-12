import numpy as np
import pandas as pd

s = pd.Series([1,1,1,2,2,2,3,3,4,4,5,6,7,7,np.NaN])

len(s)
s.size
s.shape

s.unique()
s.count()

a = np.array([2,2,2,2,np.NaN])
a.mean()

b = pd.Series(a)
b.mean()	#NaN 무시

s.value_counts()	#빈도

s[[5,7,8]]	#각각의 index 가져옴

s.head(n=7)	#상위 7개
s.tail()	#하위 5개


