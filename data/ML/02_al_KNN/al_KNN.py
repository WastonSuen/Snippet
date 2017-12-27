# coding=utf-8
"""
@version: 2017/12/26 026
@author: Suen
@contact: sunzh95@hotmail.com
@file: al_KNN
@time: 16:39
@note:  ??
"""
#

from sklearn import neighbors
from sklearn import datasets

if __name__ == '__main__':
    knn = neighbors.KNeighborsClassifier()
    iris = datasets.load_iris()
    # print(iris)
    knn.fit(iris.data, iris.target)
    predict_target = knn.predict([[0.1, 0.2, 0.3, 0.4]])
    print(predict_target)
