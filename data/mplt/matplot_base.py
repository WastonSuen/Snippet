# coding=utf-8
"""
@version: 2017/11/18 018
@author: Suen
@contact: sunzh95@hotmail.com
@file: matplot_base
@time: 12:20
@note:  ??
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

## examples scatter 散点图
# height = np.array([161, 170, 182, 175, 173, 165])
# weight = np.array([50, 58, 80, 70, 69, 55])
# plt.scatter(height, weight)

# N = 1000
# x = np.random.randn(N)
# y = np.random.randn(N)
# plt.scatter(x, y, s=500, c='r', marker='.', alpha=0.5)  # alpha 透明度

# date, closep, openp = np.loadtxt(str('000001.csv'), converters={0: mdates.strpdate2num('%Y/%m/%d')},
#                                  delimiter=str(','), skiprows=1, usecols=[0, 1, 4], unpack=True)

# plot_date default to draw scatter, need to define the fmt='-' or some other looks to make it draw with broken line
# plt.plot_date(date, openp, fmt='--', marker='.', c='r')
# plt.plot_date(date, closep, fmt='-', marker='.', c='g')
# plt.plot_date(date, closep - openp, fmt='.', c='r')

## examples broken line 折线图
# x = np.linspace(-10, 10, 5)
# y = np.square(x)
# plt.plot(x, y)

## examples bar 条形图，显示分组对比情况
# index = np.arange(5)
# value = np.array([10, 20, 50, 30, 35])
# value2 = np.array([20, 15, 40, 35, 60])
# value3 = np.array([5, 15, 25, 20, 15])
# bar horizontal水平
# plt.bar(x=0, bottom=index, width=value, height=0.4, orientation='horizontal') #not recommended
# plt.barh(y=index, width=value, height=0.4)  # recommended

## bar vertical 竖直
# plt.bar(x=index, height=value, width=0.3, color='r')

## side-by-side bar 并排
# bar_width = 0.3
# plt.bar(x=index, height=value, width=0.3, color='r')
# plt.bar(x=index + bar_width, height=value2, width=0.3, color='g')

## 堆叠
# plt.bar(x=index, height=value, width=0.3, color='r')
# plt.bar(bottom=value, x=index, height=value2, width=0.3, color='g')
# plt.bar(bottom=value + value2, x=index, height=value3, width=0.3, color='y')

## examples histogram 直方图，index轴连续，y轴为频率, 显示变化情况
# mu = 100
# sigma = 20
# x = mu + sigma * np.random.randn(20000)
# plt.hist(x, bins=100, color='g', normed=True)
# normed = True to show the frequency percentage(times/total), False to show the times

## histogram 2D 2d直方图，联合分布对比
# x = np.random.randn(20000) + 2
# y = np.random.randn(20000) + 3
# plt.hist2d(x, y, bins=20)

## pie 饼状图
# labels = ['A', 'B', 'C', 'D']
# values = [15, 20, 18, 25]
# explode = [0, 0, 0, 0]  # 远离中心,突出显示
# explode[values.index(min(values))] = 0.2  # 取出values最小值突出显示
# plt.axes(aspect=1)
# plt.pie(x=values, labels=labels, autopct='%.0f%%', explode=explode, shadow=True)


## box plot 箱形图
# data = np.random.normal(size=(1000, 4), loc=20, scale=2)
# labels = ['A', 'B', 'C', 'D']
# plt.boxplot(data, labels=labels, sym='+', whis=1.5)

## color, point shape, line shape 颜色, 点型, 线型
x = np.arange(20)
plt.plot(x, x * 2, 'rx--')
plt.plot(x, x * 3, 'g.-.')
plt.plot(x, x * 4, 'co:')
plt.plot(x, x, 'kp-')

if __name__ == '__main__':
    plt.show()

    ## could use this method following to draw in web
    # web.header('content-type', 'image/jpg') #set header format
    # cimage = cStringIO.StringIO()  # create a StringIO buffer to receive the converted image
    # fig.savefig(cimage, format="jpg")  # reformat the image into the cimage buffer
    # cimage.seek(0)
    # return cimage.read()
