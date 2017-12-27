# coding=utf-8
"""
@version: 2017/12/23 023
@author: Suen
@contact: sunzh95@hotmail.com
@file: t.py
@time: 15:30
@note:  ??
"""
import codecs
import csv


def parsestopwords():
    with codecs.open('stop.txt', 'r', 'utf_8_sig') as f:
        with codecs.open('stop_words.txt', 'wb+', 'utf_8_sig') as f2:
            writer = csv.writer(f2)
            for line in f.readlines():
                line = line.strip()
                writer.writerow(line)


if __name__ == '__main__':
    parsestopwords()
