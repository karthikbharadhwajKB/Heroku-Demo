import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('SAT.csv')

x = dataset.drop('GPA',axis=1)

x.Attendance = x.Attendance.map({'Yes':1,'No':0})

print(x.head())

y = dataset['GPA']

from sklearn.linear_model import LinearRegression 

reg = LinearRegression()

reg.fit(x,y)


pickle.dump(reg,open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))


print(model.predict([[1789,1]]))
