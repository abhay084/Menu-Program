import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')

y = dataset['Salary']

x = dataset['YearsExperience']







