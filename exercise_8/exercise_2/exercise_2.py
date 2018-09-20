a = 1
b = 2
c = 3
d = 4
li = [a,b,c,d]
for i in range(4):
    hun = li[i] * 100
    for j in range(4):
        ten = li[j] * 10
        for w in range(4):
            one = li[w]
            if (li[i] == li[j]) or (li[w] == li[j]) or (li[w] == li[i]):
                continue
            sum = hun + ten + one
            print (sum)