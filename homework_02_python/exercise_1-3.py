# -*- coding: utf-8 -*-
import numpy as ny
a = ny.array([[int(bin(n+m)[-1]) for n in range(8)] for m in range(8)])
print(a)