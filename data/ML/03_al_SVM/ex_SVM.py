# coding=utf-8
"""
@version: 2017/12/27 027
@author: Suen
@contact: sunzh95@hotmail.com
@file: ex_SVM
@time: 10:16
@note:  ??
"""

from sklearn import svm
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [[2, 0], [1, 1], [2, 3]]
    y = [0, 0, 1]
    variable_x = [v[0] for v in x]
    variable_y = [v[1] for v in x]
    plt.scatter(variable_x, variable_y)
    for xx, yy in zip(x, y):
        xx[1] += 0.05
        plt.text(*xx, yy)
        xx[1] -= 0.05
    plt.style.use('ggplot')
    # plt.show()

    clf = svm.SVC(kernel='linear')
    clf.fit(x, y)
    print(clf.support_vectors_)  # support-vector,支持向量点
    print(clf.support_)  # support-vector's index in all points支持向量点在所有点的索引
    print(clf.n_support_)  # every label's support-vector's number 从各分类中选取向量点的数量

    print(clf.predict([[1, 2], [2, 4], [3, 1]]))
