# coding=utf-8
"""
@version: 2018/1/12 012
@author: Suen
@contact: sunzh95@hotmail.com
@file: bayes_baging_desc
@time: 10:04
@note:  baging-of-words-model,词袋模型, 计算词出现次数。Multinomial Naive Bayes
与set模型不同之处: 
    0.数据集转向量vec_row[vocabulary.index(word)] += 1; 
    1.数据集sum(train_vec[i, train_vec[i] >= 1]).
"""
import csv
import codecs

import collections
import numpy as np


def load_dataset():
    dataset = np.array([['dog', 'dog', 'cat', 1],
                        ['fish', 'shark', 'dolphin', 0],
                        ['elephant', 'lion', 'dog', 1],
                        ['fish', 'fish', 'carp', 0],
                        ['pig', 'sheep', 'cow', 1],
                        ['whale', 'fish', 'dorado', 0],
                        ['bird', 'owl', 'duck', 2],
                        ['bird', 'swallow', 'bird', 2],
                        ['sparrow', 'magpie', 'crow', 2]
                        ])

    train_set = dataset[:, :-1]
    train_target = np.array(dataset[:, -1], dtype=np.int32)
    return train_set, train_target


def load_vocabulary(data):
    words_set = set([])
    for row in data:
        words_set |= set(row)

    return sorted(list(words_set))


def dataset2vec(vocabulary, dataset):
    vec = []
    for row in dataset:
        vec_row = [0] * len(vocabulary)
        for word in row:
            if word in vocabulary:
                vec_row[vocabulary.index(word)] += 1
            else:
                pass
        vec.append(vec_row)
    return np.array(vec)


def write_to_csv(vocabulary, result_dict, filename='train.csv'):
    with codecs.open(filename, 'wb+', 'utf_8_sig') as f:
        writer = csv.writer(f)
        writer.writerow(list(vocabulary) + ['LABEL'])
        for k, v in result_dict.items():
            writer.writerow(v + [k])


def bayes_training(train_vec, train_target, vocabulary):
    num_train_docs = len(train_vec)
    num_words = len(train_vec[0])
    targets_count = collections.Counter(train_target)
    targets = targets_count.keys()
    targets_dict = {target: targets_count.get(target) / len(train_target) for target in targets}

    result = {}
    for i in range(num_train_docs):
        for target in targets:
            result.setdefault(target, [np.ones(num_words), len(vocabulary)])  # 类条件概率
            # 按理论来说,上式应为 result.setdefault(target, [np.zeros(num_words), 0]), 先验概率
            # 但是, 如果某词未在文档中出现,则p(w|c)为0,为避免这种情况,采用上述做法
            if train_target[i] == target:
                result[target][0] += train_vec[i]
                result[target][1] += sum(train_vec[i, train_vec[i] >= 1])

    for k, v in result.items():
        result[k] = list(np.log(v[0] / float(v[1])))
        # 按理论来说,上式应为 result[k] = list(v[0] / float(v[1]))
        # 但是, 因均是->0的数, 在预测数据时, 每行值与向量相乘, 易导致下溢出, 为避免这种情况,采用上述取对数做法
    return result, targets_dict


def bayes_testing(result_dict, targets_dict, test_vec):
    assert len(result_dict) == len(targets_dict)
    predictions = [collections.Counter() for _ in range(len(test_vec))]
    for i in range(len(test_vec)):
        for target, p in targets_dict.items():
            predictions[i].setdefault(target, np.array(result_dict[target]).dot(test_vec[i]) + np.log(p))
    for i in range(len(predictions)):
        predictions[i] = predictions[i].most_common(1)[0][0]
    return predictions


def main():
    train_set, train_target = load_dataset()
    vocabulary = load_vocabulary(train_set)
    trainvec = dataset2vec(vocabulary, train_set)
    print(trainvec)
    test_set = [['dog', 'pig', 'boar'],
                ['fish', 'salmon', 'dolphin'],
                ['sparrow', 'swan', 'roc']
                ]
    test_target = [1, 0, 2]
    testvec = dataset2vec(vocabulary, test_set)
    print(vocabulary)
    result_dict, targets_dict = bayes_training(trainvec, train_target, vocabulary)
    # write_to_csv(vocabulary, result_dict)
    predictions = bayes_testing(result_dict, targets_dict, testvec)
    print('\nneed to be classified:\n\t', test_set)
    print('true target:\n\t', test_target)
    print('predictions:\n\t', predictions)


if __name__ == '__main__':
    main()
