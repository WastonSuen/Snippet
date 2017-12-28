# coding=utf-8
"""
@version: 2017/12/28 028
@author: Suen
@contact: sunzh95@hotmail.com
@file: al_simple_linear_regression
@time: 10:22
@note:  ??
"""

import numpy as np


def fitSLR(x, y):
    """
    simple linear regression
    :return: 
    """
    n_rows = len(x)
    denominator = 0
    numerator = 0
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    for i in range(n_rows):
        numerator += (x[i] - x_mean) * (y[i] - y_mean)
        denominator += (x[i] - x_mean) ** 2
    b1 = float(numerator) / denominator
    b0 = y_mean - b1 * x_mean
    return b0, b1


def predict(b0, b1, x):
    return b0 + b1 * x


if __name__ == '__main__':
    x = [1, 3, 2, 1, 3]
    y = [14, 24, 18, 17, 27]
    b0, b1 = fitSLR(x, y)
    print(predict(b0, b1, 8))
