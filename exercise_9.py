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
                if list_1[k] == '' or list_1[k] == '\n':
                    empty += 1
            rec.write('Number of empty lines: '+ str(empty)+ '\n')
            for j in range(len(list_1)):
                if list_1[j] == '' or list_1[j] == '\n':
                    list_1[j] ='aaaaa'
                if list_1[j].strip()[0] == '#':
                    note += 1
            rec.write('Number of note lines: '+ str(note)+ '\n')
            f.close()
            rec.close()
