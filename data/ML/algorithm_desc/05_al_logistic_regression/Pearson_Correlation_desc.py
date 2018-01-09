# coding=utf-8
"""
@version: 2018/1/1
@author: Suen
@contact: sunzh95@hotmail.com
@file: Pearson_Correlation_desc
@time: 20:59
@note:  ??
"""

import numpy as np
import math


def compute_correlation(x, y):
    """相关系数"""
    x_bar = np.mean(x)
    y_bar = np.mean(y)
    SSR = 0
    var_x = 0
    var_y = 0
    for i in range(len(x)):
        diff_x_bar = x[i] - x_bar
        diff_y_bar = y[i] - y_bar
        SSR += diff_x_bar * diff_y_bar
        var_x += diff_x_bar ** 2
        var_y += diff_y_bar ** 2

    SST = math.sqrt(var_x * var_y)
    return SSR / SST


def polyfit(x, y, degree):
    result = {}
    coeffs = np.polyfit(x, y, degree)
    result['polynomial'] = coeffs.tolist()
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y) / len(y)
    ssregression = np.sum((yhat - ybar) ** 2)
    sstotal = np.sum((y - ybar) ** 2)
    result['determination'] = ssregression / sstotal
    return result


if __name__ == '__main__':
    x = np.array([1, 3, 8, 7, 9])
    y = np.array([10, 12, 24, 21, 34])
    r = compute_correlation(x, y)
    print('r  : %s\n' % r)
    print('for linear regression:\n\tr^2: %s' % r ** 2)
    print(polyfit(x, y, degree=1))
