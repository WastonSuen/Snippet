# coding=utf-8
"""
@version: 2017/12/20 020
@author: Suen
@contact: sunzh95@hotmail.com
@file: collaborative_filtering
@time: 17:08
@note:  ??
"""

import os
from surprise import KNNBasic, Reader
from surprise import Dataset
from surprise import evaluate, print_perf

if __name__ == '__main__':
    file_path = os.path.expanduser('./ml-100k/ml-100k/u.data')
    reader = Reader(line_format='user item rating timestamp', sep='\t')

    data = Dataset.load_from_file(file_path, reader)
    data.split(n_folds=3)
    algo = KNNBasic(user_based=False)
    perf = evaluate(algo=algo, data=data, measures=['RMSE', 'MAE'])
    print_perf(perf)
