# -*- coding:UTF-8 -*-
"""
作者：TigerNiu
日期：2021年11月11日
最小二乘法python实现
"""
import numpy as np
x = np.linspace(0, 100, 200)
noise = np.random.normal(loc=0, scale=20, size=200)
# 高斯正态分布，中轴值，方差，个数
y = 3*x + 10 + noise

import matplotlib.pyplot as plt
