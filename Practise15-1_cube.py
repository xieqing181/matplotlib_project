#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
    edgecolor='1', s=40)

#set x,y lable
plt.title("前五个数的立方根", fontsize=24)
plt.xlabel("数字", fontsize=14)
plt.ylabel("立方根", fontsize=14)

#set the problem to show chinese
#指定默认字体  
plt.rcParams['font.sans-serif'] = ['FangSong']   
plt.rcParams['font.family']='sans-serif'  
#解决负号'-'显示为方块的问题  
plt.rcParams['axes.unicode_minus'] = False 

plt.axis([0, 8, 0, 150])

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
#plt.savefig("前五个数的平方根", bbox_inches='tight')
