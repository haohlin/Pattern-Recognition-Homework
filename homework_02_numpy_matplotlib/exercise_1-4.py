# -*- coding: utf-8 -*-
#自己输入有点麻烦，就先拿例子当输入了
#求解:
#3x + 4y + 2z = 10
#5x + 3y + 4z = 14
#8x + 2y + 7z = 20
import numpy as ny
coe = ny.matrix([[3,4,2], [5,3,4], [8,2,7]])
nHomo = ny.matrix([[10,14,20]])
#方法1
nHomo_T = nHomo.T
re1 = coe.I * nHomo_T
x = round(re1[0,0])
y = round(re1[1,0])
z = round(re1[2,0])
print ('方法1：\n','x= ',x,'\ny= ',y,'\nz=',z,'\n')

#方法2
re2 = nHomo * coe.T.I 
x = round(re2[0,0])
y = round(re2[0,1])
z = round(re2[0,2])
print ('方法2：\n','x= ',x,'\ny= ',y,'\nz=',z,'\n')

