# 识别验证码
#-----------------------------
# 执行要求：
#   1. 当前目录下需要有clf.model,即用神经网络训练好的模型
#   2. 当前目录有验证码图片
#-----------------------------
# 输出：
#   打印识别出来的验证码
#-----------------------------

import numpy as np
from sklearn.externals import joblib

def predict(fn):
    # 处理图片
    tx = Main(fn)
    tx = np.column_stack((tx,np.ones((4,1))))
    code = ''

    # load 训练好的神经网络模型
    nn_model = 'clf.model'
    clf = joblib.load(nn_model)
    # 识别
    yp = clf.predict(tx)
    # 转成字符
    for i in range(4):
        if yp[i] in range(0,10):
            code += chr(int(yp[i])+48)
        else:
            code += chr(int(yp[i])+87)
    print(code,end='')
    return code


if __name__ == '__main__':
    from Data import *
    # 验证码图片路径
    import sys
    #fn = sys.argv[1]
    #----------------
    #一下代码在node服务器调用
    import os
    path = sys.argv[1]
    f0 = os.listdir(path)
    fn = ''
    fl = [f for f in f0 if (len(f) >= 18 and f[0:14] == 'CheckCode.aspx')]
    if len(fl) == 1:
        fn = path + fl[0]
    else:
        fl.sort(key=lambda f: os.path.getmtime(path+f) if not os.path.isdir(path+f) else 0)
        fn = path + fl[-1]
    #---------------- 
    predict(fn)
