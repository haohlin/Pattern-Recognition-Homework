
# Pratice Report(9/19/2018)

## 林昊晗，2015300010

## EXERCISE 1

给定一个文章，找出每个单词的出现次数

One is always on a strange road, watching strange scenery and listening to strange music. Then one day, you will find that the things you try hard to forget are already gone.


```python
text = open("text.txt","r+") #打开文件（读写）
cont = text.readline() 
s1 = cont.replace(".","")    #去掉.
s2 = s1.replace(",","")      #去掉,
list1 = s2.split(" ")        #string分成list
for i in range(len(list1)):
    a = 0
    for j in range(i-1):
        if list1[i] == list1[j] : 
            a = 1
            break                 
    if a :
        continue             #除去重复计数项
    print (list1[i], list1.count(list1[i])) #循环输出每个词及每个词出现的次数
text.close()
```

思路：打开文件-读取一行字-将逗号句号用空字符代替-split处理过的字符串，使之成为以单词为元素的list-利用嵌套循环，判断输出的单词是否在之前出现过。如果是，则去掉。 <br> 涉及到的函数：<br>open（'file_name', 'open_as'）<br>f.readline():  读取一行数据为字符串，包括换行符<br>str.replace('a','b'):  将字符串中的a换成b<br>str.split('a'):  以a为划分标准，将字符串分割成列表<br>len():  字符串、列表、元组等中元素的个数，但不包含空字符null<br>list.count('a'):  列表中a元素出现的次数

## EXERCISE 2

有 1、2、3、4 个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？


```python
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
```

    123
    124
    132
    134
    142
    143
    213
    214
    231
    234
    241
    243
    312
    314
    321
    324
    341
    342
    412
    413
    421
    423
    431
    432
    

将1,2,3,4放到list中，通过三个for嵌套循环对四个数字实现排列组合。每次循环得到一个三位数，判断各位数字不相等后输出此数字。

## EXERCISE 3

企业发放的奖金根据利润提成。利润(I)：

低于或等于 10 万元时，奖金可提 10%；
<br>高于 10 万元，低于 20 万元时，低于 10 万元的部分按 10%提成，高于 10 万元的部分，可提成 7.5%；
<br>20 万到 40 万之间时，高于 20 万元的部分，可提成 5%；
<br>40 万到 60 万之间时，高于 40 万元的部分，可提成 3%；
<br>60 万到 100 万之间时，高于 60 万元的部分，可提成 1.5%，
<br>高于 100 万元时， 超过 100 万元的部分按 1%提成， 从键盘输入当月利润 I，求应发放奖金总数？


```python
a = int(input('salary= '))
w = 100000
if a <= w:
    bonus = 0.1*a
elif a < 2*w:
    bonus = 0.1*w + (a-w)*0.075
elif a < 4*w:
    bonus = 0.1*w + 0.075*w + (a - 2*w)*0.05
elif a < 6*w:
    bonus = 0.1*w + 0.075*w + 2*w*0.05 + (a - 4*w)*0.03
elif a < 10*w:
    bonus = 0.1*w + 0.075*w + 2*w*0.05 + 2*w*0.03 + (a - 6*w)*0.015
else : bonus = 0.1*w + 0.075*w + 2*w*0.05 + 2*w*0.03 + 4*w*0.015 + (a - 10*w)*0.01
print(bonus)
```

    salary= 345243
    24762.15
    

输入利润后判断奖金。难度不大。

## EXERCISE 4

输出9x9的乘法口诀表


```python
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
            #排列整齐口诀表，如果得数位数等于一，则加一位空格
        if k==8 :
            print('\n')
```

        1    2    3    4    5    6    7    8    9    
    
    1   1    2    3    4    5    6    7    8    9    
    
    2   2    4    6    8    10   12   14   16   18   
    
    3   3    6    9    12   15   18   21   24   27   
    
    4   4    8    12   16   20   24   28   32   36   
    
    5   5    10   15   20   25   30   35   40   45   
    
    6   6    12   18   24   30   36   42   48   54   
    
    7   7    14   21   28   35   42   49   56   63   
    
    8   8    16   24   32   40   48   56   64   72   
    
    9   9    18   27   36   45   54   63   72   81   
    
    

其他好说，重点在于输出漂亮的乘法表的格式，因为二位数会打乱行列一一对应关系。做以判断如果得数是一位数，自动补一个空格。<br>用到的函数：<br>str():    将数或列表变成字符串，列表会包含方括号和标点。<br>print(something, end = ''):     意为输出后不自动换行

## EXERCISE 5

使用while循环实现输出2-3+4-5+6.....+100的和


```python
import math
sum_1 = 0
for i in range(2,101):
    s = i*math.pow(-1, i)
    sum_1 = int(s) + sum_1
print(sum_1)
```

    51
    

难度不大。<br>函数：<br>pow(x,y):x的y次方

## EXERCISE 6

给一个数字列表，将其按照由大到小的顺序排列

例如

1, 10, 4, 2, 9, 2, 34, 5, 9, 8, 5, 0


```python
list_1 = [1, 10, 4, 2, 9, 2, 34, 5, 9, 8, 5, 0]
print(list_1)
for i in range(len(list_1)-1):
    for j in range(len(list_1)-(i+1)):
        if list_1[j] < list_1[-(i+1)]:
            a = list_1[-(i+1)]
            list_1[-(i+1)] = list_1[j]
            list_1[j] = a
print(list_1)
```

    [1, 10, 4, 2, 9, 2, 34, 5, 9, 8, 5, 0]
    [34, 10, 9, 9, 8, 5, 5, 4, 2, 2, 1, 0]
    

基本的冒泡排序，从大到小排列。外循环是倒着选一个数，内循环是从头选数与外循环选得数对比，如果后面的数大则二者调换，反之不变。这样得到的最后一位一定是最小的。接下来换倒数第二个数与之前的每一个比较，循环往复直到第一位与第二位比较完毕。

## EXERCISE 7

做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

需要考虑什么是激活码？有什么特性？例如KR603guyVvR是一个激活码


```python
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
```

    KA38Owk21rZ0cXKoca6l
    

这个题挺有意思。产生一个包含大小写字母和数字的20位序列号。使用random.randint(a,b)能产生[a,b]区间的一个随机整数，但要在大写、小写和数字的ASCII码区间中随机产生一个数无法实现，因为这三者的ASCII码不是连续的。因此只能先随机选大小写数字其中之一，然后再在相应ASCII区间中随机生成int。Python好像没有switch case语句，只能用if代替了。<br>函数：<br>chr()：将十进制或十六进制转换成ACSII字符。<br>str1.join(list1)：将list1中的各个元素用str1链接为一个字符串。

## EXERCISE 8

需要把某个目录下面所有的某种类型的文件找到。 例如把c:下面所有的.dll文件找到


```python
import os

for root, dire, file in os.walk("F:\OneDrive\文档\jupyter notebook\exercise_8"):  
                                   #exercise_8所在路径
    for i in range(len(file)):
        if file[i].split('.')[-1] == 'py':
            print(file[i])

```

实现起来比较简单，因为os.walk()函数太方便了，直接得到文件夹中所有文件或文件夹的路径、文件夹及文件。通过遍历即可得到所有文件名。老师说的递归用的是os.listdir()函数。有空试试。得到的file是每一级目录中文件名组成的列表，用for循环将列表中每个名字用'.'分开，得到的list的倒数第一个元素就是后缀。判断如果后缀是py则输出文件名。

## EXERCISE 9

你有个目录，里面是程序（假如是C或者是Python），统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。


```python
import os

for root, dire, file in os.walk("F:\OneDrive\文档\jupyter notebook"):
    for i in range(len(file)):
        if file[i].split('.')[-1] == 'py':
            note = 0
            empty = 0
            f = open(root+'/'+file[i], 'r', encoding='UTF-8')
            rec = open('RECORD.txt', 'a')
            l = 0
            list_1 = f.readlines()
            rec.write(file[i] + ':\n' + 'Total number of lines: '+ str(len(list_1)) + '\n')
            for k in range(len(list_1)):
                if  list_1[k] == '\n':
                    empty += 1
            rec.write('Number of empty lines: '+ str(empty)+ '\n')
            for j in range(len(list_1)):
                if list_1[j] == '\n':
                    list_1[j] ='aaaaa'
                if list_1[j].strip()[0] == '#':
                    note += 1
            rec.write('Number of note lines: '+ str(note)+ '\n')
            f.close()
            rec.close()
```

这个题我想多了！！！用了半天来调bug，结果发现根本不是bug。因为文本文档的最后一行不是空字符串，事实上它根本不存在！详情见截图：

![截图](捕获.PNG)

第九题用到了前一题的代码。找到目录里所有的.py文件并打开（打开时加一段encoding='UTF-8'，否则因为有特殊字符会报错）。用f.readlines()得到一个list，其中每个元素是每一行的字符串型式，包含\n行，不包含最后一行空字符串。len(list)即总行数。然后用for循环判断每一行是不是只有\n(空行)，然后对每一行进行str.strip()去掉首尾空格后，判断第一个字符是不是'#'来确定注释行。最后以指针在文件末尾、追加模式建立RECORD.txt，记录每个.py文件的总行数、空行数和注释行数。然后如果对'\n'进行strip操作后取第0位会报错，所以我就把空行随便赋了个值:)<br>函数：<br>os.walk('path')：得到一个包含path、文件夹名和文件名的object，通过遍历可以得到每一个文件的path和名字。<br>f.write('str')：写，但末尾没有\n

## 小结

这是我第一次用Python写代码，函数记不住只能来回查，浪费好多时间。以后要多多练习，熟能生巧！而且可能有很多代码可以用更简洁、更快速的方法实现，在这方面我要向老师多多学习。希望老师批评指正。