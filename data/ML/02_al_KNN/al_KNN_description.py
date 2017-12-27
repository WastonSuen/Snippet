# coding=utf-8
"""
@version: 2017/12/26 026
@author: Suen
@contact: sunzh95@hotmail.com
@file: al_KNN_description
@time: 16:37
@note:  optimize: 优化：使用1/dis来代表每个距离的权重
"""
import operator
import os
import csv
import math
import codecs
import random

import collections


def load_dataset(filepath, split):
    """加载数据集"""
    if not os.path.exists(filepath):
        return []
    training_list = []
    testing_list = []
    with codecs.open(filepath, 'r+', 'utf_8_sig') as f:
        reader = csv.reader(f)
        dataset = list(reader)
        for row in dataset:
            for ncol in range(len(row) - 1):
                row[ncol] = float(row[ncol])
            if random.random() > split:
                testing_list.append(row)
            else:
                training_list.append(row)
    return training_list, testing_list


def enclidean_distance(ins1, ins2):
    """两点向量的欧几里得距离"""
    distance = 0
    for v1, v2 in zip(ins1[:-1], ins2[:-1]):
        distance += pow((v2 - v1), 2)
    return math.sqrt(distance)


def get_neighbors(training_list, instance, k):
    """获取k个近邻集"""
    distances = []
    for training_ins in training_list:
        dis = enclidean_distance(training_ins, instance)
        distances.append((training_ins, dis))
    distances.sort(key=operator.itemgetter(1))
    return [distances[i] for i in range(k)]


def vote_neighbors(neighbors):
    """计算最优解"""
    nb_labels = [nb[-1] for nb in neighbors]
    counter = collections.Counter(nb_labels)
    label = counter.most_common(1)
    return label[0][0]


def vote_neighbors_optimize(neighbors):
    """使用1/dis优化最优解"""
    total_distance = sum([nb[1] for nb in neighbors])
    distance_weight = [total_distance / float(nb[1] + 1) for nb in neighbors]
    total_weight = sum(distance_weight)
    weight = [float(dis_weight) / total_weight for dis_weight in distance_weight]
    label_dict = dict()
    for x in range(len(neighbors)):
        label = neighbors[x][0][-1]
        label_dict.setdefault(label, 0)
        label_dict[label] += weight[x]
    counter = collections.Counter(**label_dict)
    label = counter.most_common(1)
    return label[0][0]


def get_acccuracy(testing_list, predictions):
    """获得正确率"""
    total = len(testing_list)
    correct = 0
    for testing_ins, prediction_ins in zip(testing_list, predictions):
        if testing_ins[-1] == prediction_ins:
            correct += 1
    return float(correct) / total * 100.0


if __name__ == '__main__':
    training_list, testing_list = load_dataset('./iris.csv', 0.67)
    k = 3
    predictions = []
    for testing_ins in testing_list:
        neighbors = get_neighbors(training_list, testing_ins, k)
        neighbors_without_dis = [nb[0] for nb in neighbors]
        label = vote_neighbors(neighbors_without_dis)
        predictions.append(label)
    accuracy = get_acccuracy(testing_list, predictions)
    print('before optimizition:%0.3f%%' % accuracy)

    optimize_predictions = []
    for testing_ins in testing_list:
        neighbors = get_neighbors(training_list, testing_ins, k)
        label = vote_neighbors_optimize(neighbors)
        optimize_predictions.append(label)
    optimize_accuracy = get_acccuracy(testing_list, predictions)
    print('after optimizition:%0.3f%%' % optimize_accuracy)
