#coding:utf-8

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()

    rw.fill_walk()
    
    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap=plt.cm.Blues, s=15)


    plt.title("随机漫步", fontsize=24)
    plt.xlabel("横向", fontsize=14)
    plt.ylabel("纵向", fontsize=14)

    #set the problem to show chinese
    #指定默认字体  
    plt.rcParams['font.sans-serif'] = ['FangSong']   
    plt.rcParams['font.family']='sans-serif'  
    #解决负号'-'显示为方块的问题  
    plt.rcParams['axes.unicode_minus'] = False 

    #plt.axis([0, 1000, 0, 100])

    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.show()
    
    keep_running = input("make another walk? (y/n): ")
    if keep_running == 'n':
        break
