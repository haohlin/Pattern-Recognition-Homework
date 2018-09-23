import numpy as np
import matplotlib.pyplot as plt
import math

#在[0,2pi]取100个随机方向
dirc = np.random.random(100)*2*np.pi

#竖向排列两个图，第一个为极坐标，第二个为直角坐标
fig, ax = plt.subplots(2,1)

#极坐标下展现了每步的方向和大小（定为单位步长），用每个点与原点连线组成的向量表示
ax[0] = plt.subplot(211, projection='polar')
for i in range(100):
    ax[0].plot([dirc[i],dirc[i]],[0,1],'r')

#初始化x
x = np.random.rand(100)
x[0] = 0
a = 0
#初始化y
y = np.random.rand(100)
y[0] = 0
b = 0
#每一步在x的投影为cos(dirx[i]), 在y的投影为sin(dirx[i])，然后将每一步连起来即为走过的路径
for i in range(1,100):
    a += math.cos(dirc[i-1])
    x[i] = a
    b += math.sin(dirc[i-1])
    y[i] = b
    
ax[1].plot(x,y,marker='+',markeredgecolor="red")
#处理坐标轴，使起点位于原点（坐标轴交点）
ax[1].xaxis.set_ticks_position("bottom")
ax[1].yaxis.set_ticks_position("left")
ax[1].spines["bottom"].set_position(('data',0))
ax[1].spines["left"].set_position(('data',0))
ax[1].spines["right"].set_color("none")
ax[1].spines["top"].set_color("none")

fig.savefig('exercise_2-3.pdf')