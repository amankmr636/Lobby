import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df=pd.read_csv('data.csv')

Xtrain,Xtest,Ytrain,Ytest=train_test_split(df[['age']],df['target'],test_size=0.2)

model=LogisticRegression()
model.fit(Xtrain,Ytrain)


pre=model.predict(Xtest)
print(pre)
pre2=model.predict([[77]])
pre3=model.predict([[7]])
print(pre2,pre3)

