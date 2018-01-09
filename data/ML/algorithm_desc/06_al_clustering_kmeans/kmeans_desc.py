# coding=utf-8
"""
@version: 2018/1/1
@author: Suen
@contact: sunzh95@hotmail.com
@file: kmeans_desc
@time: 22:42
@note:  ??
"""
import collections
import numpy as np
import matplotlib.pyplot as plt


def get_label(data_row, centroids):
    label = centroids[0, -1]
    min_distance = np.linalg.norm(data_row - centroids[0, :-1])
    for i in range(1, centroids.shape[0]):
        distance = np.linalg.norm(data_row - centroids[i, :-1])
        if distance < min_distance:
            label = centroids[i][-1]
            min_distance = distance
    return label


def update_labels(dataset, centroids):
    row, col = np.shape(dataset)
    for i in range(row):
        dataset[i, -1] = get_label(dataset[i, :-1], centroids)


def new_centroids(dataset, k):
    result = np.zeros((k, dataset.shape[1]))
    for kk in range(1, k + 1):
        old_cluster = dataset[dataset[:, -1] == kk, :-1]
        result[kk - 1, :-1] = np.mean(old_cluster, axis=0)
        result[kk - 1, -1] = kk
    return result


def stop_now(temp_centroids, centroids, i, max_iteration):
    if i >= max_iteration:
        return True
    if np.array_equal(temp_centroids, centroids):
        return True


def kmeans(x, k, max_iteration):
    row, col = np.shape(x)
    dataset = np.zeros((row, col + 1))
    dataset[:, :-1] = x

    centroids = dataset[np.random.randint(row, size=k), :]  # random choice centroids
    centroids[:, -1] = range(1, k + 1)  # 1 to k labels

    temp = None
    i = 0
    while not stop_now(temp, centroids, i, max_iteration):
        print('iteration: %s\n' % i)
        print('centroids: %s\n' % centroids)
        temp = np.copy(centroids)
        update_labels(dataset, centroids)
        centroids = new_centroids(dataset, k)
        i += 1
    return dataset


def plot_dataset(dataset):
    datadict = collections.defaultdict(list)
    for row in dataset: datadict[row[-1]].append(row[:-1])

    for k, v in datadict.items():
        draw_x = []
        draw_y = []
        for row in v:
            draw_x.append(row[0])
            draw_y.append(row[1])
        plt.scatter(draw_x, draw_y)
    plt.show()


if __name__ == '__main__':
    x = np.array([[1, 1], [2, 1], [4, 3], [5, 4]])
    dataset = kmeans(x, 2, 10)
    print('dataset: %s\n' % dataset)
    plot_dataset(dataset)
