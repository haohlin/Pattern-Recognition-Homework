from keras.models import Model #将各个层组合成全连接神经网络的函数
from keras.layers import Input, Dense #构建各层用到的函数
from keras.utils import np_utils
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

batch_size = 20000 #每次训练用到的数据规模
num_epochs = 40 #训练次数
hidden_size = 50 #隐藏层节点数
num_train = 200000 #训练样本数
spe_len = 36 #每个样本参数数量
num_classes = 2 #二分类

#读取数据集
train_data = np.array(pd.read_csv('train.csv'))
test_data = np.array(pd.read_csv('test.csv'))
X_train = train_data[:,1:-1]
X_train = X_train.astype('float32') #源数据是int类型，这里需要转换成float
y_train = train_data[:,-1]
#由于是二分类问题，输出层有两个节点，所以需要将label处理成两列。
Y_train = np_utils.to_categorical(y_train, num_classes)
X_test = test_data[:,1:]

'''创建输入层，隐藏层1、2，输出层并建立先后顺序关系。
两个隐藏层节点数和激活函数相同。
注意到两个隐藏层和输出层都有bias，可以使预测模型更精确。
输出层激活函数是softmax。'''
inp = Input(shape=(spe_len,)) 
hidden_1 = Dense(hidden_size, activation='relu', use_bias = True)(inp) 
hidden_2 = Dense(hidden_size, activation='relu', use_bias = True)(hidden_1)
out = Dense(num_classes, activation='softmax', use_bias = True)(hidden_2)

#用Model函数将上述各层连接到一起
model = Model(inputs=inp, outputs=out)

'''定义好模型之后需要通过编译来对学习过程进行配置，
我们可以为模型的编译指定各类参数包括：优化器optimizer，损失函数loss，评估指标metrics'''
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

'''采用反向传播算法训练神经网络。训练完成后，history 会保存模型训练后的相关描述'''
history = model.fit(X_train, Y_train, batch_size=batch_size, epochs=num_epochs, verbose=1, validation_split=0.1)

# 绘制训练和测试精度曲线
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# 绘制训练和测试损失函数曲线
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

#对测试集进行预测
test_predict = model.predict_on_batch(X_test)
test_predict = test_predict[:,0]
print(test_predict) 

#将预测输出到submit_data.csv中
submitData = pd.read_csv("submit_data.csv")
submitData['Evaluation'] = test_predict
submitData.to_csv("submit_data.csv", index=False)