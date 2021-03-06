#importing libraries
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
# visualization
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

test_df = pd.read_csv('projects/test.csv')
train_df = pd.read_csv('projects/train.csv')

combine = [train_df, test_df]

for dataset in combine:
    dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
    
for dataset in combine:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col',\
 	'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')

    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')
    
train_df[['Title', 'Age']].groupby(['Title'], as_index=False)

for index in range(0,len(train_df)):
  missing = train_df['Age'][index]
  if missing >=0:
    pass
  else:
    if train_df['Title'][index] == 'Master':
      train_df['Age'][index]=3.5
    if train_df['Title'][index] == 'Miss':
      train_df['Age'][index]=21
    if train_df['Title'][index] == 'Mr':
      train_df['Age'][index]=30
    if train_df['Title'][index] == 'Mrs':
      train_df['Age'][index]=35
    if train_df['Title'][index] == 'Rare':
      train_df['Age'][index]=48.5
      
      
for index in range(0,len(test_df)):
  missing = test_df['Age'][index]
  if missing >=0:
    pass
  else:
    if test_df['Title'][index] == 'Master':
      test_df['Age'][index]=3.5
    if test_df['Title'][index] == 'Miss':
      test_df['Age'][index]=21
    if test_df['Title'][index] == 'Mr':
      test_df['Age'][index]=30
    if test_df['Title'][index] == 'Mrs':
      test_df['Age'][index]=35
    if test_df['Title'][index] == 'Rare':
      test_df['Age'][index]=48.5
      
train_df['Embarked'] = train_df['Embarked'].replace(np.nan, 's')
test_df['Embarked'] = test_df['Embarked'].replace(np.nan, 's')

###################for test_df fare###############
for index in range(0,len(test_df)):
  missing=test_df['Fare'][index]
  if missing >=0:
    pass
  else:
    test_df['Fare'][index]=35.6
    
###################for test_df fare############### 

for index in range(0,len(train_df)):
  missing = train_df['Age'][index]
  if missing >=0:
    pass
  else:
    test_df['Age'][index]=35.6
    
    
###########Label encode for test gender########
labelencoder_x = LabelEncoder()
train_df['Sex'] = labelencoder_x.fit_transform(train_df['Sex'])
train_df['Embarked'] = labelencoder_x.fit_transform(train_df['Embarked'])

test_df['Sex'] = labelencoder_x.fit_transform(test_df['Sex'])
test_df['Embarked'] = labelencoder_x.fit_transform(test_df['Embarked'])


train_df.drop(['PassengerId','Name','Cabin','Ticket','Title'],axis=1, inplace=True)
test_df.drop(['PassengerId','Name','Cabin','Ticket','Title'],axis=1, inplace=True)

train_df_x=train_df[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]
train_df_y=train_df[['Survived']]

x_train,x_test,y_train, y_test = train_test_split(train_df_x,train_df_y, test_size =0.0000001, random_state=0)
x_test= test_df[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(x_train, y_train)

trial = [[3,1,30.0,	0,	0,	7.55,	2]]
y_pred = random_forest.predict(trial)
print(y_pred)
