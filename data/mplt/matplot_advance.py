# coding=utf-8
"""
@version: 2017/11/18 018
@author: Suen
@contact: sunzh95@hotmail.com
@file: matplot_advance
@time: 15:29
@note:  ??
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)

## subplot 子图
# fig = plt.figure()
# axis1 = fig.add_subplot(221)
# axis1.plot(x, x, 'r')
# axis2 = fig.add_subplot(222)
# axis2.plot(x, -x, 'r')
# axis3 = fig.add_subplot(223)
# axis3.plot(-x, x, 'r')
# axis4 = fig.add_subplot(224)
# axis4.plot(-x, -x, 'r')

## gridding 网格
# fig = plt.figure()
# axis = fig.add_subplot(111)
# axis.grid()  # active grid only
# axis.grid(color='g', linewidth=0.2, linestyle='--')  # active grid and set the properties
# axis.plot(x)


## legend 图例
# fig = plt.figure()
# axis = fig.add_subplot(111)
# axis.plot(x * 2, 'r.--')
# axis.plot(x * 3, 'gx-.')
# axis.plot(x * 4, 'b>:')
# label = 'Double', 'Triple', 'Quadruple'
# axis.legend(labels=label, loc=0, ncol=2)
## loc 0 is the adaptation, loc(1,2,3,4) is the sector 象限. ncol is the colums of legend


##range of axis 坐标轴范围
# fig = plt.figure()
# axis = fig.add_subplot(111)
# axis.plot(x, x)
# axis.axis([5, 10, 0, 8])# method 1

# axis.set_xlim(left=5, right=10)
# axis.set_ylim(bottom=0, top=8)#method 2

##axis locator 坐标轴分布
# fig = plt.figure()
# axis = fig.add_subplot(111)
# axis.plot(x, x)
# axis.locator_params('x', nbins=10)
# axis.locator_params(nbins=10)  # both

##date 日期
# import datetime
# from matplotlib import dates as mdates
#
# fig = plt.figure()
# axis = fig.add_subplot(111)
# start = datetime.datetime(2017, 1, 1)
# end = datetime.datetime(2018, 1, 1)
# delta = datetime.timedelta(days=1)
# dates = mdates.drange(start, end, delta)
# y = np.random.rand(len(dates))
# date_format = mdates.DateFormatter('%y-%m')
# axis.xaxis.set_major_formatter(date_format)
# fig.autofmt_xdate()  # dont cover each other, 时间坐标不互相遮挡, 自适应
# axis.plot_date(dates, y, 'g.-')


##sharing axis X or Y 公用x轴或y轴
# fig = plt.figure()
# axis1 = fig.add_subplot(111)
# axis1.plot(x, x ** 2)
# axis1.set_ylabel('Y1')
# axis1.set_xlabel('SHARING X')
# axis2 = axis1.twinx()
# axis2.plot(x, np.log(x), 'r.--')
# axis2.set_ylabel('Y2')


## other projection 其他图像
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='polar')
# r = np.arange(0, 1, 0.001)
# theta = 2 * 2 * np.pi * r
# line, = ax.plot(theta, r, color='#ee8d18', lw=3)  # lw is linewidth
#
# ind = 800
# thisr, thistheta = r[ind], theta[ind]
# ax.plot([thistheta], [thisr], 'o')
# ax.annotate('a polar annotation',
#             xy=(thistheta, thisr),  # theta, radius
#             xytext=(0.05, 0.05),  # fraction, fraction
#             textcoords='figure fraction',
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             horizontalalignment='left',
#             verticalalignment='bottom',
#             )

## annotate 注释
# fig = plt.figure()
# axis = fig.add_subplot(111)
# axis.plot(x, x ** 2, 'g.-')
# axis.text(-8, 90, 'function: y = x^2', size=20, family='fantasy', style='italic', weight=800,  # 粗细, 字体, 样式, 深浅
#           bbox=dict(color='r', alpha=0.02)  # 框, 颜色, 深浅,
#           )
# axis.annotate('bottom', xy=(0, 1), xytext=(2, 20),
#               arrowprops=dict(facecolor='r', shrink=0.05),
#               horizontalalignment='left',  # 水平对齐
#               verticalalignment='bottom',  # 垂直对齐
#               )

## Tex 数学公式
## http://matplotlib.org/users/mathtext.html
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_xlim(0, 10)
# ax.set_ylim(0, 10)
# ax.text(2, 2, r'$\alpha_i > \beta_i$')
# ax.text(8, 8, r'$\sin(0)=\cos(\frac{\pi}{2})%$')
# ax.text(2, 8, r'$\sum_{i=0}^\infty x_i$')
# ax.text(8, 2, r'$\sqrt[3]{x}$')

##fill 填充
# fig = plt.figure()
# axis = fig.add_subplot(111)

# t = np.arange(-np.pi, np.pi, 0.01)
# y1 = np.sin(t * 2)
# y2 = np.sin(t * 3)
# could remove the two rows following, to hide the side line
# axis.plot(t, y1, 'r')
# axis.plot(t, y2, 'b')
# axis.fill(t, y1, 'r', alpha=0.1, interpolate=True)
# axis.fill(t, y2, 'b', alpha=0.1, interpolate=True)

##fill between
# axis.fill_between(t, y1, y2, where=y1 > y2, facecolors='r', alpha=0.4, interpolate=True)
# axis.fill_between(t, y1, y2, where=y1 < y2, facecolors='b', alpha=0.4, interpolate=True)

##style 美化图像
# print plt.style.available
# plt.style.use("ggplot")

if __name__ == '__main__':
    plt.show()
