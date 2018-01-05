# coding=utf-8
"""
@version: 2018/1/5 005
@author: Suen
@contact: sunzh95@hotmail.com
@file: analyse
@time: 11:43
@note:  ??
"""

import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import KFold, cross_val_score


def fetch_data(filename='train.csv'):
    dataset = pd.read_csv(filename)
    dataset.drop(['Name', 'Cabin', 'Ticket', 'PassengerId'], axis=1, inplace=True)
    dataset.fillna({'Age': dataset['Age'].mean()}, inplace=True)  # dataset['Age'].fillna(dataset.Age.mean())

    dataset['Sex'][dataset['Sex'] == 'male'] = 1  # dataset.loc[dataset['Sex'] == 'male', 'Sex'] = 1
    dataset['Sex'][dataset['Sex'] == 'female'] = 0
    dataset.fillna({'Embarked': dataset['Embarked'].describe().top}, inplace=True)
    dataset['Embarked'][dataset['Embarked'] == 'S'] = 0
    dataset['Embarked'][dataset['Embarked'] == 'C'] = 1
    dataset['Embarked'][dataset['Embarked'] == 'Q'] = 2

    dataset.fillna({'Fare': dataset['Fare'].mean()}, inplace=True)
    # dataset['Fare'].as_type(np.int32)
    # print(dataset.head())
    # print(dataset.describe())
    return dataset


def decision_tree(dataset, predictors):
    alg = DecisionTreeClassifier()
    kf = KFold(n_splits=10, random_state=1)
    scores = cross_val_score(alg, dataset[predictors], dataset['Survived'], cv=kf)
    print('decision tree: %0.5f%%' % (scores.mean() * 100))
    return scores.mean()


def linear_regression(dataset, predictors):
    alg = LinearRegression()
    kf = KFold(n_splits=10, random_state=1)
    predictions = []
    for train, test in kf.split(dataset[predictors]):
        train_predictors = (dataset[predictors].iloc[train, :])
        train_target = dataset['Survived'].iloc[train]
        alg.fit(train_predictors, train_target)
        test_predictions = alg.predict(dataset[predictors].iloc[test, :])
        predictions.append(test_predictions)

    predictions = np.concatenate(predictions, axis=0)
    predictions[predictions > .5] = 1
    predictions[predictions <= .5] = 0
    accuracy = len(predictions[predictions == dataset['Survived']]) / len(predictions)
    print('linear regression: %0.5f%%' % (accuracy * 100))
    return accuracy


def logistic_regression(dataset, predictors):
    alg = LogisticRegression(random_state=1)
    kf = KFold(n_splits=10, random_state=1)
    scores = cross_val_score(alg, dataset[predictors], dataset['Survived'], cv=kf)
    print('logistic regression: %0.5f%%' % (scores.mean() * 100))
    return scores.mean()


def random_forest_classifier(dataset, predictors):
    alg = RandomForestClassifier(random_state=1, n_estimators=80, min_samples_leaf=2, min_samples_split=4)
    kf = KFold(n_splits=10, random_state=1)
    scores = cross_val_score(alg, dataset[predictors], dataset['Survived'], cv=kf)
    print('random forest clf: %0.5f%%' % (scores.mean() * 100))
    return scores.mean()


def random_forest_predict(trainset, predictors, testset, target):
    alg = RandomForestClassifier(random_state=1, n_estimators=80, min_samples_leaf=2, min_samples_split=4)
    alg.fit(trainset[predictors], trainset['Survived'])
    predictions = alg.predict(testset[predictors])
    accuracy = len(predictions[predictions == target['Survived']]) / len(testset)
    print('random forest accuracy: %0.5f%%' % (accuracy * 100))

    total_survived = len(target[target['Survived'] == 1])
    predictions_correct = predictions[predictions == target['Survived']]
    TP = len(predictions_correct[predictions_correct == 1])
    recall = TP / total_survived
    print('random forest recall: %0.5f%%' % (recall * 100))


def main():
    predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    trainset = fetch_data('train.csv')
    testset = fetch_data('test.csv')
    target = pd.read_csv('target.csv')
    print(trainset.head())
    print(testset.describe())
    decision_tree(trainset, predictors)
    linear_regression(trainset, predictors)
    logistic_regression(trainset, predictors)
    random_forest_classifier(trainset, predictors)
    print('%s*' % ('*-' * 24))
    random_forest_predict(trainset, predictors, testset, target)
    print('%s*' % ('*-' * 24))


if __name__ == '__main__':
    main()
