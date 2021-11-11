# -*- coding:UTF-8 -*-
"""
作者：TigerNiu
日期：2021年11月11日
最小二乘法python实现
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 200)
noise = np.random.normal(loc=0, scale=10, size=200)
# 高斯正态分布，中轴值，方差，个数
y = 3*x + 10 + noise


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(x, y, c='c')
plt.title('b站用户投币-颜值关系图')
plt.xlabel('b站用户投币数')
plt.ylabel('up主颜值')
plt.show()

def computer_L(w, b, x, y):
    loss_total = 0
    for i in range(len(x)):
        loss_total += (w*x[i] + b - y[i])**2
    return loss_total

def average(data):
    count = 0
    for i in range(len(data)):
        count += data[i]
    return count/len(data)

def fix(x, y):
    up = 0
    down = 0
    x_bar = average(x)
    y_bar = average(y)

    for i in range(len(x)):
        up += (x[i] - x_bar)*(y[i] - y_bar)
        down += (x[i] - x_bar)**2

    w = up/down

    b = y_bar - w * x_bar
    return w, b
w, b = fix(x, y)
print('w is', w)
print('b is', b)