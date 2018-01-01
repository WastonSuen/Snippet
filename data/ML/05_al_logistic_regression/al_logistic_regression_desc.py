# coding=utf-8
"""
@version: 2018/1/1
@author: Suen
@contact: sunzh95@hotmail.com
@file: al_logistic_regression_desc
@time: 16:27
@note:  ??
"""

import numpy as np
import random


def gen_data(num_points, bias, variance):
    x = np.zeros(shape=(num_points, 2))
    y = np.zeros(shape=(num_points, 1))
    for i in range(num_points):
        x[i][0] = 1
        x[i][1] = i

        y[i] = (i + bias) + random.uniform(0, 1) * variance
    return x, y


def gradient_descent(x, y, theta, alpha, row, num_iteration):
    """
    梯度下降算法
    :param x:
    :param y:
    :param theta:初始向量值
    :param alpha:学习率
    :param row: 每次迭代下降次数
    :param num_iteration:迭代次数
    :return:向量值
    """
    x_trans = x.transpose()
    for i in range(num_iteration):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        cost = np.sum(loss ** 2) / (2 * row)
        assert isinstance(cost,float)
        print('iteration:%05d, | cost:%s' % (i, cost))
        gradient = np.dot(x_trans, loss) / row
        theta = theta - alpha * gradient
    return theta


if __name__ == '__main__':
    x, y = gen_data(100, 25, 10)
    row, col = np.shape(x)
    row_y, col_y = np.shape(y)

    num_iteration = 100000
    alpha = 0.0005
    theta = np.ones(col)
    theta = gradient_descent(x, y[:, 0], theta, alpha, row, num_iteration)
    print(theta)
