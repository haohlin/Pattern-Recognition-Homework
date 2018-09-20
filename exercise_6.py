list_1 = [1, 10, 4, 2, 9, 2, 34, 5, 9, 8, 5, 0]
print(list_1)
for i in range(len(list_1)-1):
    for j in range(len(list_1)-(i+1)):
        if list_1[j] < list_1[-(i+1)]:
            a = list_1[-(i+1)]
            list_1[-(i+1)] = list_1[j]
            list_1[j] = a
print(list_1)