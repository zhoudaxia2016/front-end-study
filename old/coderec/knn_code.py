import numpy as np

# 将oneOfk变成0，1，2...
def getLabel(Y):
    r,c = Y.shape
    y = np.ravel(np.zeros((1,r)))
    for i in range(r):
        m = 0
        for j in range(c):
            if Y[i,j] == 1:
                m = j
                break
        y[i] = m
    return y
# 测试 非oneOfk形式
def test1(y,yp):
    err = 0
    l = len(y)
    for i in range(l):
        if y[i] != yp[i]:
            err += 1
    return err/l

# load data
X = np.loadtxt('/home/maozz/prml/code/code/w.txt')
y = np.loadtxt('/home/maozz/prml/code/code/Type.txt')
r,c = X.shape

# knn
k = getLabel(y)
from sklearn import neighbors

knn = neighbors.KNeighborsClassifier(n_neighbors = 1)
knn.fit(X,k)

# load one test picture
from PIL import Image
fn = '/home/maozz/coderec/code.jpg'
fn = '/home/maozz/prml/code/code/验证码数据集/1111code.jpg'

from Data import *
tx = Main(fn)
yp = knn.predict(tx)
code = ''
for i in range(4):
    if yp[i] in range(0,10):
        code += chr(int(yp[i])+48)
    else:
        code += chr(int(yp[i])+87)

import json
data = {'code':code}
print(data)

