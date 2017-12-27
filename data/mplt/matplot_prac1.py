# coding=utf-8
"""
@version: 2017/11/21 021
@author: Suen
@contact: sunzh95@hotmail.com
@file: matplot_prac1
@time: 10:24
@note:  math plot
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def func(x):
    return -(x - 2) * (x - 8) + 40


x = np.linspace(0, 10, 1000)
y = func(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, 'r', linewidth=2)

a = 2
b = 9
ax.set_xticks([a, b])
ax.set_xticklabels(['$a$', '$b$'])
ax.set_yticks([])

plt.figtext(0.92, 0.08, '$x$')  # percentage on the x or y axis
plt.figtext(0.1, 0.9, '$y$')

ix = np.linspace(a, b, 1000)
iy = func(ix)

verts = [(a, 0)] + zip(ix, iy) + [(b, 0)]
polygon = Polygon(verts, facecolor='0.8')
ax.add_patch(polygon)

ax.text(sum([a, b]) / 3, sum(ax.get_ylim()) / 2, r'$\int_a^b-(x - 2) * (x - 8) + 40$')

if __name__ == '__main__':
    plt.show()
