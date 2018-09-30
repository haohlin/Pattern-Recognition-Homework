# -*- coding: utf-8 -*-
import numpy as np
a = np.arange(16).reshape(4,4)
print(a, '\n')
b = a[::-1,::-1]
print(b)
