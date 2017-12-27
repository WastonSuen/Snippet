# coding=utf-8
"""
@version: 2017/12/20 020
@author: Suen
@contact: sunzh95@hotmail.com
@file: t.py
@time: 18:01
@note:  ??
"""

import os

from surprise import AlgoBase, Reader
from surprise import Dataset
from surprise import evaluate

class MyOwnAlgorithm(AlgoBase):
    def __init__(self):
        # Always call base method before doing anything.
        super(MyOwnAlgorithm, self).__init__()

    def estimate(self, u, i):
        return 3


if __name__ == '__main__':
    file_path = os.path.expanduser('./ml-100k/ml-100k/u.data')
    reader = Reader(line_format='user item rating timestamp', sep='\t')
    data = Dataset.load_from_file(file_path=file_path, reader=reader)
    algo = MyOwnAlgorithm()

    evaluate(algo, data)
