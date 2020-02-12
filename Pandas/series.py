import numpy as np
import pandas as pd

s1 = pd.Series([1,2,3])
s2 = pd.Series(['a','b'.'c'])
s3 = pd.Series(np.arrange(200))
pd.Series([1,2,3], [100,200,300])

#index string able 

s6=pd.Series(np.arrange(5), np.arrange(100,105), dtype=np.int16)
s6.index
s6.values

s6[104]

s6[104]=70

s7 = pd.Series(np.arrange(7), s6.index)




