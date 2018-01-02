# coding=utf-8
"""
@version: 2018/1/2 002
@author: Suen
@contact: sunzh95@hotmail.com
@file: digits_recognition_hand_written.py
@time: 14:50
@note:  ??
"""

import numpy as np
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import LabelBinarizer
from .neural_network_desc import NeuralNetwork
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    digits = load_digits()
    x = digits.data
    rows, cols = x.shape
    print('rows: {}\ncols: {}'.format(rows, cols))
    y = digits.target

    # normalize
    x -= x.min()
    x /= x.max()

    nn = NeuralNetwork([64, 100, 10], 'logistic')
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
    labels_train = LabelBinarizer().fit_transform(y_train)
    labels_test = LabelBinarizer().fit_transform(y_test)
    print('starting fitting data......')
    nn.fit(x_train, labels_train, epochs=300000)
    print('done fitting data\n')
    predictions = []
    for row in x_test:
        a = nn.predict(row)
        predictions.append(np.argmax(a))
    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))
