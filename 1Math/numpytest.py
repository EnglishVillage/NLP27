#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

a=np.arange(0,60,10).reshape((-1,1))+np.arange(6)
print(a)
# [[ 0  1  2  3  4  5]
#  [10 11 12 13 14 15]
#  [20 21 22 23 24 25]
#  [30 31 32 33 34 35]
#  [40 41 42 43 44 45]
#  [50 51 52 53 54 55]]

ls=range(10)
ls[1:4]=10,20,30
print ls

myls=[]
myls.append(map(float,"230.1,23.2,12.4".split(",")))
print(myls)