import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-16,16,32)
y = x**2
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y)

#plot第一个变量意思是x范围取定在一点，而y的范围在0到y[i]
for i in range(32):
    axes.plot([x[i],x[i]],[0,y[i]],'r')

axes.set_title(r'$y = x^2$')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.xaxis.set_ticks_position("bottom")
axes.spines["bottom"].set_position(('data',0))