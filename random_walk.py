#coding: utf-8

from random import choice


class RandomWalk():
    '''一个生成随机数的类'''
    def __init__(self, num_points=5000):
        self.num_points = num_points
        #所有随机数都始于0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''计算随机漫步的所有点'''
        
        #不断漫步，直到列表达到指定长度
        while len(self.x_values) < self.num_points:
            #decide move direction and distance
            x_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            #avoid maintain the same place
            if x_step == 0 & y_step == 0:
                continue
            
            x_next = self.x_values[-1] + x_step
            y_next = self.y_values[-1] + y_step
            
            self.x_values.append(x_next)
            self.y_values.append(y_next)


