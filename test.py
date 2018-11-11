# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

dataset = pd.read_csv('Salary_Data.csv')
dataset

#预存储

'''
1.loc意义：通过行标签索引行数据
       例： loc[n]表示索引的是第n行（index 是整数）

              loc[‘d’]表示索引的是第’d’行（index 是字符）

   2. .iloc   ：通过行号获取行数据，不能是字符

   3.  ix——结合前两种的混合索引
'''
X = dataset.iloc[:, :-1].values
print (X)

y = dataset.iloc[:, 1].values
print (y)

#shu ju fen ger
from  sklearn.model_selection import train_test_split
# 注意下面的test_size = 1/3的时候会报错的
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)


# make model
from sklearn.linear_model import LinearRegression
# use the package to make model
regressor = LinearRegression()
# fit means feed?
regressor.fit(X_train, y_train)

y_pre = regressor.predict(X_test)

print (dataset)

print (y_pre)

# 数据可视化
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train,regressor.predict(X_train), color='blue')
plt.title("Salary VS Years") # 不能用中文？
plt.xlabel('Years')
plt.ylabel('Salary')
plt.show()
