text = open("text.txt","r+") #打开文件（读写）
cont = text.readline() 
s1 = cont.replace(".","") #去掉.
s2 = s1.replace(",","") #去掉,
list1 = s2.split(" ") #string分成list
for i in range(len(list1)):
    a = 0
    for j in range(i-1):
        if list1[i] == list1[j] : 
            a = 1
            break                 
    if a :
        continue                   #除去重复计数项
    print (list1[i], list1.count(list1[i])) #循环输出每个词及每个词出现的次数