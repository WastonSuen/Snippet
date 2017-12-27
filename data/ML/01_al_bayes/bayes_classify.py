# coding=utf-8
"""
@version: 2017/12/25 025
@author: Suen
@contact: sunzh95@hotmail.com
@file: bayes_classify
@time: 10:46
@note:  ??
"""

import csv
import codecs
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

if __name__ == '__main__':
    feature_list = []
    labellist = []
    with codecs.open('bayes_classify_dataset.csv', 'r', 'utf_8') as f:
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            if i == 0:
                header = row
                continue
            labellist.append(row[len(row) - 1])
            rowdict = dict()
            for i in range(1, len(row) - 1):
                rowdict[header[i]] = row[i]
            feature_list.append(rowdict)

    vec = DictVectorizer()
    dummy_x = vec.fit_transform(feature_list).toarray()
    print('dummy_x:{}'.format(dummy_x))
    # print(vec.get_feature_names())
    # print(labellist)

    label = preprocessing.LabelBinarizer()
    dummy_y = label.fit_transform(labellist)
    print('dummy_y:{}'.format(dummy_y))

    classifier = tree.DecisionTreeClassifier(criterion='entropy')  # ID3
    classifier.fit(dummy_x, dummy_y)
    print('classifier:{}'.format(str(classifier)))

    ## generate decision tree graph
    # with codecs.open("bayes_classify_graph.dot", 'w') as f:
    #     f = tree.export_graphviz(classifier, feature_names=vec.get_feature_names(), out_file=f)
    ## windows command line: dot -Tpdf bayes_classify_graph.dot -o bayes_classify_graph.pdf

    new_row_x = [dummy_x[0, :]]
    new_row_x[0][0], new_row_x[0][2] = 1, 0
    print('predict: %s' % classifier.predict(new_row_x))
