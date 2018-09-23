# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2,20)
y = np.exp(-x**2)*pow(np.sin(x-2),2)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)

ax.set_title(r'$y = sin^2(x-2)e^{-x^2}$')
ax.set_xlabel('x')
ax.set_xlim([0,2])
ax.set_ylabel('y')
