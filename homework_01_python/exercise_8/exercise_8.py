import os

for root, dire, file in os.walk("F:\OneDrive\文档\jupyter notebook\exercise_8"):  
                                   #exercise_8所在路径
    for i in range(len(file)):
        if file[i].split('.')[-1] == 'py':
            print(file[i])
