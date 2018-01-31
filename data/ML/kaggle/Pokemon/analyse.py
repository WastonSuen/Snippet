# coding=utf-8
"""
@version: 2018/1/22 022
@author: Suen
@contact: sunzh95@hotmail.com
@file: analyse
@time: 11:04
@note:  ??
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier


def fetch_data(filename='dataset.csv'):
    dataset = pd.read_csv(filename)
    dataset['Type'] = dataset.Type_1 + ('_' + dataset.Type_2).fillna('')
    dataset = dataset.drop(['Type_1', 'Type_2'], axis=1)

    # fig = plt.figure()
    # ax = fig.add_subplot(121, projection='polar')
    # ability_draw(dataset.drop('Type', axis=1), 'Pikachu', ax)
    # ax = fig.add_subplot(122, projection='polar')
    # ability_draw(dataset.drop('Type', axis=1), 'Zapdos', ax)
    # plt.show()

    types = dataset.Type.unique()
    for i in range(len(types)):
        dataset['Type'][dataset['Type'] == types[i]] = i
    print(dataset.head(10))
    print(dataset.describe())
    labels = np.array(dataset['Legendary'])
    return dataset.drop(['Legendary'], axis=1), dataset, labels


def random_forest_classifier(dataset, predictors, label):
    alg = RandomForestClassifier(random_state=1, n_estimators=68, min_samples_leaf=1, min_samples_split=3)
    kf = KFold(n_splits=3, random_state=1)
    scores = cross_val_score(alg, dataset[predictors], dataset[label], cv=kf)
    print('random forest clf: %0.5f%%' % (scores.mean() * 100))
    return scores.mean()


def ability_draw(dataset, name, ax):
    ability_frame = dataset[dataset['Name'] == name][:]
    dataset = ability_frame.drop(['Name', '#', 'Generation', 'Generation', 'Legendary', 'Total'], axis=1)
    labels = dataset.columns.values
    values = dataset.values[0]

    theta = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    theta = np.append(theta, theta[0])
    values = np.append(values, values[0])
    font = FontProperties(fname=r'C:\Windows\Fonts\STFANGSO.TTF')
    ax.plot(theta, values, color='r')
    ax.fill(theta, values, 'r', alpha=0.3)
    ax.set_xticks(theta)
    ax.set_xticklabels(labels, fontproperties=font)
    ax.set_title(name)


if __name__ == '__main__':
    dataset, whole, labels = fetch_data()
    print(whole.describe())
    predictors = dataset.columns.drop(['Name', '#'])
    random_forest_classifier(whole, predictors, 'Legendary')
