import pandas as pd

#dict
data ={'a': 100, 'b':200, 'c':300}
pd.DataFrame(data, index=['x','y','z'])

data ={'a':[1,2,3], 'b':[4,5,6], 'c': [10,11,12]}
pd.DataFrame(data, index=['x','y','z'])

#series
a = pd.Series([100,200,300], ['a','b','c'])
b = pd.Series([101,201,301], ['a','b','k'])

pd.DataFrame([a,b,c], index=[100,101,102])





