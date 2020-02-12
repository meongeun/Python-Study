import pandas as pd

train_data = pd.read_csv('./train.csv')

train_data.head(n=3)	#상위 3개 출력
train_data.tail()

train_data.shape
train_data.describe()	#통계값 출력

train_data.info()	#type& 갯수

train_data.index	# RangeIndex	0부터 시작
train_data.columns	#열의 리스트





