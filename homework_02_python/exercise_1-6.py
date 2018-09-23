# -*- coding: utf-8 -*-
import numpy as np
a = np.random.randint(0,100,(10,10))
print (a)
b = np.where( a == a.max())
print ('max:',a.max(),'\nLocation:')
for i in range (len(b[0])):
    print(b[0][i], b[1][i])
    
print('\n')

c = np.where( a == a.min())
print ('min:',a.min(),'\nLocation:')
for j in range (len(c[0])):
    print(c[0][j], c[1][j])
