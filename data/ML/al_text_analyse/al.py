# coding=utf-8
"""
@version: 2017/12/23 023
@author: Suen
@contact: sunzh95@hotmail.com
@file: al
@time: 11:33
@note:  ??
"""
import codecs
import csv
import jieba
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from lxml import etree


def fetch_data():
    """
    fetch the contenttitle and the content from the news xml doc
    :return: [(title,content)......]
    """
    tree = etree.parse('smarty.xml')
    title = tree.xpath('//contenttitle')
    content = tree.xpath('//content')
    info = [(t.text, c.text) for t, c in zip(title, content)]
    return info


def store_info(info_list):
    with codecs.open('news.csv', 'wb+', 'utf_8_sig') as f:
        writer = csv.writer(f)
        writer.writerow(['theme', 'content'])
        for row in info_list:
            writer.writerow(row)


def process_data():
    df_news_total = pd.read_csv('smarty_news.csv')
    df_news = df_news_total[:160]
    df_news = df_news.dropna()
    content = df_news.content.values.tolist()

    content_words = []
    for line in content:
        current_segment = jieba.lcut(line)
        if len(current_segment) > 1 and current_segment != '\r\n':
            content_words.append(current_segment)

    df_content = pd.DataFrame({'content_words': content_words})
    return df_content, content_words


def drop_stopwords(content_words):
    df_stopwords = pd.read_csv('stop_words.txt', index_col=False, sep='\n', quoting=3, names=['stopword'])
    stopwords = df_stopwords.stopword.values.tolist()
    content_words_clean = []
    all_words = []
    for line in content_words:
        linewords = []
        for word in line:
            if word in stopwords or word == u'\ue40c':
                continue
            linewords.append(word)
            all_words.append(word)
        content_words_clean.append(linewords)
    return content_words_clean, all_words


def analyse_all_words(all_words):
    df_allwords = pd.DataFrame({'all_words': all_words})
    words_count = df_allwords.groupby(by=['all_words'])['all_words'].agg(('count', np.size))
    words_count = words_count.reset_index().sort_values(by=['count'], ascending=False)

    wordcloud = WordCloud(font_path=r'C:\Windows\Fonts\STFANGSO.TTF', background_color='white', max_font_size=80)
    word_frequence = {x[0]: x[1] for x in words_count.head(100).values.tolist()}
    print(word_frequence)
    wordcloud = wordcloud.fit_words(word_frequence)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


def main():
    # infolist = fetch_data()
    # store_info(infolist)
    df_content, content_words = process_data()
    content_words_clean, all_words = drop_stopwords(content_words)
    df_content = pd.DataFrame({'content_words_clean': content_words_clean})
    analyse_all_words(all_words)


if __name__ == '__main__':
    main()
