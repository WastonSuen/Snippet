# coding=utf-8
"""
@version: 2017/12/27 027
@author: Suen
@contact: sunzh95@hotmail.com
@file: al_SVM
@time: 10:11
@note:  ??
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

if __name__ == '__main__':
    np.random.seed(0)
    x = np.r_[(np.random.rand(20, 2) - 2), (np.random.rand(20, 2) + 2)]
    y = np.array([0] * 20 + [1] * 20)
    # scatter
    scatter_x = [v[0] for v in x]
    scatter_y = [v[1] for v in x]
    # for i in range(len(y)):
    #     plt.text(*x[i], y[i])

    clf = svm.SVC(kernel='linear')
    clf.fit(x, y)

    # hyperplane
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5, 100)
    yy = a * xx - clf.intercept_[0] / w[1]

    # lower hyperplane
    b = clf.support_vectors_[0]
    yy_down = a * xx + (b[1] - a * b[0])
    b = clf.support_vectors_[-1]
    yy_up = a * xx + (b[1] - a * b[0])

    plt.ylim([-5, 5])
    plt.xlim([-5, 5])
    plt.scatter(scatter_x[:20], scatter_y[:20], color='g', alpha=0.4)
    plt.scatter(scatter_x[20:], scatter_y[20:], color='b', alpha=0.4)
    plt.plot(xx, yy, 'r-')
    plt.plot(xx, yy_down, 'g--', alpha=0.2)
    plt.plot(xx, yy_up, 'b--', alpha=0.2)
    plt.style.use('ggplot')
    plt.show()
