import random
str_1=[None] * 20
for i in range(20):
    a = random.randint(1, 3)
    if a==1:
        str_1[i] = chr(random.randint(48, 57))
        continue
    if a==2: 
        str_1[i] = chr(random.randint(65, 90))
        continue
    if a==3: 
        str_1[i] = chr(random.randint(97, 122))
        continue
print("".join(str_1)) 
