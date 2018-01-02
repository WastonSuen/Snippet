# coding=utf-8
"""
@version: 2018/1/2 002
@author: Suen
@contact: sunzh95@hotmail.com
@file: neural_network_desc
@time: 10:26
@note:  ??
"""

import numpy as np


def tanh(x):
    return np.tanh(x)


def tanh_deriv(x):
    """ tanh derivative """
    return 1 - np.tanh(x) * np.tanh(x)


def logistic(x):
    return 1 / (1 + np.exp(-x))


def logistic_deriv(x):
    return logistic(x) * (1 - logistic(x))


class NeuralNetwork(object):
    def __init__(self, layers, activation='logistic'):
        """
        :param layers: list of each layer's number, including the input layer  
        :param activation: sigmoid function
        """
        self.activation, self.activation_deriv = (tanh, tanh_deriv) \
            if activation == 'tanh' else (logistic, logistic_deriv)
        self.weights = []
        for i in range(1, len(layers) - 1):
            self.weights.append((2 * np.random.random((layers[i - 1] + 1, layers[i] + 1)) - 1) * 0.25)
            self.weights.append((2 * np.random.random((layers[i] + 1, layers[i + 1])) - 1) * 0.25)

    def fit(self, x, y, learning_rate=0.2, epochs=10000):
        """
        :param x: 
        :param y: 
        :param learning_rate: 学习率
        :param epochs:数据量大，抽取epochs个数据进行训练，相当于预设训练次数 
        :return: 
        """
        x = np.atleast_2d(x)
        rows, cols = np.shape(x)
        temp = np.ones((rows, cols + 1))
        temp[:, :-1] = x
        x = temp

        y = np.array(y)
        for k in range(epochs):
            i = np.random.randint(rows)
            a = [x[i]]

            for l in range(len(self.weights)):
                a.append(self.activation(np.dot(a[l], self.weights[l])))
            # list a contains each layer's value
            err = y[i] - a[-1]
            deltas = [err * self.activation_deriv(a[-1])]  # output layer's delta, type: list of list

            # inverse, backpropagation
            for l in range(len(a) - 2, 0, -1):
                deltas.append(deltas[-1].dot(self.weights[l].T) * self.activation_deriv(a[l]))
            deltas.reverse()

            # update weights
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

    def predict(self, x):
        x = np.array(x)
        temp = np.ones(x.shape[0] + 1)
        temp[0:-1] = x
        a = temp
        for l in range(len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a


if __name__ == '__main__':
    """XOR"""
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])

    nn = NeuralNetwork([2, 2, 1], 'tanh')
    nn.fit(x, y)
    for row in x:
        result = [0 if line < 0.5 else 1 for line in nn.predict(row)]
        print('{} ==> {}'.format(row, *result))
