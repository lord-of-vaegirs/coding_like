"""
matplotlib库

手册：https://matplotlib.org/stable/plot_types/index.html

plot函数连点成线 两个参数分别为列表 存放对应的x和y值

title函数 可以标明图像的名称

xlabel 标明x轴的名称
ylabel 标明y轴名称

show函数用于展示图表

scatter 用于标出点来
scatter(x,y,marker='',c='')
marker表示点的显示 c表示颜色
c='r' 表示红色
marker='*' 点就按*显示

plot(x,y,linestyle='',label='')
label是给图线上标签 得用legend语句让他显示
linestyle改变图线样式 --是虚线 默认实线

"""

import matplotlib.pyplot as plt
# 下面三行是更改字体的代码 可以使中文显示 且为黑体
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

import numpy as np


x=np.linspace(0,10,10)
# print(x)

y=np.sin(x)

# print(y)

x2=np.linspace(0,10,100)

y2=np.sin(x2)

# plt.scatter(x,y,c='r',label='dot')
# # 一组已知点位的数据标出
# plt.plot(x2,y2,linestyle='--',label='nihe_line')
# # 拿曲线来拟合上面的点的数据 看是否一致
#
# plt.legend()
#
# plt.title('y=sinx x>=0&x<=10')
#
# plt.xlabel('x')
#
# plt.ylabel('y')
#
#
#
# plt.show()

"""
多图绘制
"""
fig,axes=plt.subplots(1,2)
axes[0].scatter(x,y,c='r',label='dot')
axes[0].set_xlabel('x1')
axes[0].set_ylabel('y')
axes[0].set_title('doting')
axes[1].plot(x2,y2,linestyle='--',label='nihe_line')
axes[1].set_xlabel('x2')
axes[1].set_title('doting2')
fig.legend()
fig.show()
plt.show()

"""
直方图
"""

# x=[1,2,3]
# y=[2,4,10]
#
# plt.bar(x,y)
# plt.show()















































