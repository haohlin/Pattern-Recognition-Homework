import math
sum_1 = 0
for i in range(2,101):
    s = i*math.pow(-1, i)
    sum_1 = int(s) + sum_1
print(sum_1)

