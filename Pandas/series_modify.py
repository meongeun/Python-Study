import numpy as np
import pandas as pd

s = pd.Series(np.arrange(100,105), ['a','b','c','d','e'])

s.drop('k')		#복사본 반환
s
s.drop('k', inplace=True)	#바로 적용

s[['a','b']] = [300,900]

s1 = pd.Series(np.Series(np.arrange(100,105))
s1[1:3]
s2['c':'d']		#마지막 포함


	

