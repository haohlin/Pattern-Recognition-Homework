a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
list_1 = [a,b,c,d,e,f,g,h,i]
print ('    ', end='')
for j in range(len(list_1)):
    print (list_1[j], '   ', end='')
print('\n')
for j in range(len(list_1)):
    print (j + 1, '  ', end='')
    for k in range(len(list_1)):
        print (list_1[j]*list_1[k], '  ', end='')
        if len(str(list_1[j]*list_1[k])) == 1:
            print (' ', end='')            
            #排列整齐口诀表，如果得数位数小于一，则加一位空格
        if k==8 :
            print('\n')
