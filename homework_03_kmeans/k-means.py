# -*- coding: utf-8 -*-
import csv
import numpy as np
import matplotlib.pyplot as plt
from math import atan2
'''读数据'''
csvFile = open("dataset_circles.csv", "r")
reader = csv.reader(csvFile)

result = []
for item in reader:
    for i in range(3):
        item[i] = float(item[i])
    result.append(item)
result = np.array(result)

plt.scatter(result[:,0], result[:,1], c = result[:,2])#坐标变换前的数据分布
plt.title('Untransformed data')
plt.figure()
ang = []
for i in range(len(result[:,1])):
    ang_ind = atan2(result[i,1], result[i,0])
    ang.append(ang_ind)

dist_tran = np.sqrt(result[:,0]**2 + result[:,1]**2)

ang = np.array(ang)
dist_tran = np.array(dist_tran)
plt.scatter(ang, dist_tran, c = result[:,2])#坐标变换后的数据分布
plt.title('Transformed data')
plt.show()
csvFile.close()

'''定义kmeans类'''
class kmeans():
    
    def __init__(self, orig_data):
        '''初始化时传入数据，作为第一个属性'''
        self.orig_data = orig_data 

    def vote(self, center1, center2):
        '''label作为第二个属性，是移动完重心后根据距离判断得到的分类结果'''
        
        self.label = []
        for i in range(len(self.orig_data)):
            dist_indv1 = np.linalg.norm(self.orig_data[i] - center1)#i点与第一类重心的距离
            dist_indv2 = np.linalg.norm(self.orig_data[i] - center2)#i点与第二类重心的距离
            if dist_indv1 > dist_indv2:  #判断i点分类
                self.label.append(1)
            else:
                self.label.append(0)
        self.label = np.array(self.label)
    
    def performance(self, center1, center2):
        '''group_index作为第三个属性，是分类结果中同一类的所有下标。
           本函数计算分完类后各个类的性能，然后相加得到该重心时的性能'''
        
        self.vote(center1, center2)
        self.group1_index = np.argwhere(self.label == 0)    #np.argwhere(ndarray!!!)
        performance1 = np.sum((self.orig_data[self.group1_index[:,0]] - center1)**2)    #np.argwhere返回n*1的矩阵，转换成n维向量才能带入下标
        self.group2_index = np.argwhere(self.label == 1)
        performance2 = np.sum((self.orig_data[self.group2_index[:,0]] - center2)**2)
        return performance1 + performance2
    
    def move_center(self):
        '''如果性能不达标则执行此函数，即将当前重心移动到当前类的几何中心'''
        
        center1_new = np.sum(self.orig_data[self.group1_index[:,0]], axis = 0) / len(self.orig_data[self.group1_index[:,0]])
        center2_new = np.sum(self.orig_data[self.group2_index[:,0]], axis = 0) / len(self.orig_data[self.group2_index[:,0]])
        return center1_new, center2_new
        
    def score(self, label_true):
        '''评分。这里要注意的是k-means是只能把类区别开，但不能打上正确的标签。'''
        
        score = 0
        for i in range(len(label_true)):
            if label_true[i] == self.label[i]:
                score += 1
        score /= len(label_true)
        return score
    
    
data_trans = np.hstack((ang.reshape(-1,1), dist_tran.reshape(-1,1)))  #将坐标转换后的数据整理成n行2列的形式，方便读取
data_untrans = np.hstack((result[:,0].reshape(-1,1), result[:,1].reshape(-1,1)))  #原始数据
true_label = result[:,2]  #label用来评分

'''初始化未进行坐标变换的kmeans库'''
km = kmeans(data_untrans)
'''选择重心起点'''
center1 = data_untrans[1]
center2 = data_untrans[300]
performance_save1 = [0]   #将性能指标函数存入list
for i in range(10):   #循环计算性能指标函数，改变重心，并判断是否达到要求。同时如果循环次数大于10也会结束循环
    p = km.performance(center1, center2)
    performance_save1.append(p)
    if performance_save1[i+1] == performance_save1[i]:
        break    #如达标跳出循环
    else: 
        center1, center2 = km.move_center()    #不达标，则移动中心重新计算
        
label_untrans = km.label
print('score = ',km.score(true_label))    
print('predicted center = ', center1, center2)
print('predicted label = ',label_untrans)

plt.figure()
plt.scatter(result[:,0], result[:,1], c = label_untrans)
plt.title('Untransformed results')


'''初始化已进行坐标变换的kmeans库'''
km = kmeans(data_trans)
center1 = data_trans[1]
center2 = data_trans[300]
performance_save2 = [0]
for i in range(10): 
    p = km.performance(center1, center2)
    performance_save2.append(p)
    if performance_save2[i+1] == performance_save2[i]:
        break
    else: 
        center1, center2 = km.move_center()
        
label_trans = km.label
print('score = ',km.score(true_label))    
print('predicted center = ', center1, center2)
print('predicted label = ',label_trans)

plt.figure()
plt.scatter(result[:,0], result[:,1], c = label_trans)
plt.title('Transformed results')