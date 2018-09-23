# -*- coding: utf-8 -*-
import numpy as ny
m = int (input("row: "))
n = int (input("collum: "))

a = ny.random.rand(m,n)
print(a, '\n')

b = ny.zeros((m,1))

b_1 = ny.c_[b,a,b]

c = ny.zeros((1,n+2))

trans_a = ny.r_[c,b_1,c]

print(trans_a)
