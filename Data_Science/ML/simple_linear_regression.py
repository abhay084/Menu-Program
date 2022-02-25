import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')

y = dataset['Salary']

x = dataset['YearsExperience']


X = x.values.reshape(-1,1)

print(X.shape)

model = LinearRegression()
model.fit(X,y)
print(model.coef_)

print(model.intercept_)


print(model.predict[[2]])





