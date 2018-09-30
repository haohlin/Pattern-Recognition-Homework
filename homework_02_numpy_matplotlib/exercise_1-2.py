import numpy as np
a = np.random.rand(5,5)
print(a, '\n')

b = a.flatten()
print(b, '\n')

for i in range(4):
    b[5+6*i] = i + 1

b.shape = 5,5
print(b)
#or:
#a.shape = 1,-1
#print(a, '\n')

#for i in range(4):
#    a[0,5+6*i] = i + 1

#a.shape = 5,5
#print(a)