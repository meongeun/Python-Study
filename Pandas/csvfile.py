import pandas as pd

# ,로 구분한 data
train_data = pd.read_csv('./train.csv', index_col = 'PassengerId')
train_data.head()

# 원하는 column, row 

train_data[1]	#하나는 column
train_data['Survived']
train_data[['Survived', 'Age']]

#dataframe slicing

train_data[7:10]	#row이용
train_data.head()
train_data.index = np.arrange(100,991)
train_data.tails()

train_data.loc[[986, 100, 110, 990]]
train_data.iloc[0]	#0 base index

train_data.loc[[986,100,110,990], ['Surivied','Name', 'Age']]

#boolean selection

train_data.head()

class_ = train_data['Pclass'] == 1
age_ = (train_data['Age'] >= 30) & (train_data['Age'] <40)

train_data[class_ & age_]

train_data['Age Double'] = train_data['Age'] * 2
train_data.head()

train_data['Age_tripple'] train_data['Age_double']+ train_data['Age']
train_data.inser(3, 'Fare10', train_data['Fare']/10)

train_data.drop(['Age_triple','Age_tripple'], axis=1)	#행 레벨은 0 열 레벨은 1



