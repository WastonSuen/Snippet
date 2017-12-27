# coding=utf-8
"""
@version: 2017/11/23 023
@author: Suen
@contact: sunzh95@hotmail.com
@file: matplot_prac2
@time: 10:09
@note:  hist 热力图
"""

from matplotlib import pyplot as plt
import numpy as np

x = np.random.randn(400)
y = x + np.random.randn(400) * 0.5

# percentage on the axis
margin_boarder = 0.1
width = 0.6
margin_between = 0.02
height = 0.2

left_scatter = margin_boarder  # left margin
bottom_scatter = margin_boarder  # bottom margin
height_scatter = width  # height
width_scatter = width  # weight

left_hist1 = margin_boarder
bottom_hist1 = margin_boarder + width + margin_between
height_hist1 = height
width_hist1 = width

left_hist2 = margin_boarder + width + margin_between
bottom_hist2 = margin_boarder
height_hist2 = width
width_hist2 = height

plt.figure(1, figsize=(12, 12))
rect_scatter = [left_scatter, bottom_scatter, width_scatter, height_scatter]
rect_hist1 = [left_hist1, bottom_hist1, width_hist1, height_hist1]
rect_hist2 = [left_hist2, bottom_hist2, width_hist2, height_hist2]

scatter = plt.axes(rect_scatter)
scatter.scatter(x, y)

bin_width = 0.25
width = 2 * np.max([np.max(np.abs(x)), np.max(np.abs(y))])
bins = int(width / bin_width) + 1

hist1 = plt.axes(rect_hist1)
plt.hist(x, bins=bins, color='g', normed=True)
hist1.set_xticks([])
hist2 = plt.axes(rect_hist2)
plt.hist(y, bins=bins, color='r', normed=True, orientation='horizontal')
hist2.set_yticks([])

if __name__ == '__main__':
    plt.style.use("ggplot")
    plt.show()
