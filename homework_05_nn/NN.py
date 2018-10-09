import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

np.random.seed(0)
data, label = datasets.make_moons(200, noise=0.20)

'''二分类只需要一个输出节点，多分类需要超过三个节点，label初始化方法如下
t = np.zeros((X.shape[0], 2))
t[np.where(y==0), 0] = 1
t[np.where(y==1), 1] = 1'''

a = np.ones(len(data)).reshape(-1,1)
data = np.hstack((data, a))
plt.scatter(data[:, 0], data[:, 1], c=label, cmap=plt.cm.Spectral)
plt.show()

class NeuralNetwork():
    
    def __init__(self, data, true_label):
        self.data = data
        self.true_label = true_label
        
    def sigmod(self, x):
        sigmod = 1/(1+np.exp(-x))
        return sigmod
        
    def layer_1(self):
        self.net_1 = np.dot(self.data, self.w1)
        self.A_1 = self.sigmod(self.net_1)
    
    def layer_2(self):
        self.layer_1()
        self.net_2 = np.dot(self.A_1, self.w2)
        self.A_2 = self.sigmod(self.net_2)
        
    def predict(self, w1, w2):
        self.w1 = w1
        self.w2 = w2
        self.layer_2()
        self.pred = []
        for i in range(len(self.A_2)):
            if self.A_2[i] >= 0.5:
                self.pred.append(1)
            else:
                self.pred.append(0)
        return self.pred
    
    def score(self):
        score = 0
        self.f_index = []
        for i in range(len(self.pred)):
            if self.pred[i] == self.true_label[i]:
                score += 1
            else:
                self.f_index.append(i)
        score /= len(self.pred)
        return score
        
    def performance(self):
        Ed = np.sum((self.A_2 - self.true_label)**2)
        return Ed
    
    def rand_gradient(self):
        rand_index = np.random.choice(self.f_index)
        a = (self.A_2[rand_index] - self.true_label[rand_index])*self.A_2[rand_index]*(1-self.A_2[rand_index])
        grad_w2 = (a*self.A_1[rand_index]).reshape(-1,1)
        grad_w1 = a*self.w2*self.A_1[rand_index]*(1-self.A_1[rand_index])*self.data[rand_index]
        return grad_w2, grad_w1
    
w_1 = np.ones((3,3))-2
w_2 = np.ones(3).reshape(-1,1)
alpha = 0.01
n = 100000

nn = NeuralNetwork(data, label)

for i in range(n):
    pred = nn.predict(w_1, w_2)
    score = nn.score()
    performance = nn.performance()
    print(i, '      ', score, '       ', performance)
    grad = nn.rand_gradient()
    if score < 0.865:
        w_1 -= alpha*grad[1]
        w_2 -= alpha*grad[0]
    else:
        break
print(w_1, w_2)

plt.scatter(data[:, 0], data[:, 1], c=pred)
plt.figure()
plt.scatter(data[:, 0], data[:, 1], c=pred)
pred = np.array(pred)
plt.scatter(data[nn.f_index, 0], data[nn.f_index, 1], c=pred[nn.f_index], cmap=plt.cm.cool)