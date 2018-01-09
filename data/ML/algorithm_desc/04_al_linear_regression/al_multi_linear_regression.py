# coding=utf-8
"""
@version: 2017/12/28 028
@author: Suen
@contact: sunzh95@hotmail.com
@file: al_multi_linear_regression
@time: 10:33
@note:  ??
"""
import numpy as np
from sklearn import linear_model

if __name__ == '__main__':
    data = np.genfromtxt(r'slr_data.csv', delimiter=',')
    print(data)

    x = data[:, :-1]
    y = data[:, -1]

    clf = linear_model.LinearRegression()
    clf.fit(x, y)

    # ceofficients 系数
    # print(clf.coef_)
    # interception 截距
    # print(clf.intercept_)

    x_pred = [[102, 6]]
    print(x_pred),
    print('预测值: %s' % clf.predict(x_pred))
