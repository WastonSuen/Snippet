# coding=utf-8
"""
@version: 2017/12/12 012
@author: Suen
@contact: sunzh95@hotmail.com
@file: matplot_prac3
@time: 11:26
@note:  能力图
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r'C:\Windows\Fonts\STFANGSO.TTF')

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

theta = np.linspace(0, 2 * np.pi, 6, endpoint=False)
theta = np.append(theta, theta[0])

ability_label = np.array(['进攻', '防守', '生存', '法术', '物理', '移速'])
ability_value = np.random.randint(low=60, high=100, size=len(ability_label))
ability_value = np.append(ability_value, ability_value[0])

ax.plot(theta, ability_value, color='r')
ax.fill(theta, ability_value, 'r', alpha=0.3)
ax.set_xticks(theta)
ax.set_xticklabels(ability_label, fontproperties=font)

if __name__ == '__main__':
    plt.show()
