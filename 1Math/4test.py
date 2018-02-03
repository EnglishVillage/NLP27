#!/usr/bin/python
# -*- coding:utf-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np
from time import time

if __name__ == '__main__':
	# x=np.arange(0.05,3,0.05)
	# y1=[math.log(a,1.5) for a in x]
	# plt.plot(x,y1,linewidth=2,color="#007500",label="log1.5(x)")
	#
	# plt.plot([1,1],[y1[0],y1[-1]],"r--",linewidth=2)
	#
	# y2=[math.log(a,2) for a in x]
	# plt.plot(x,y2,linewidth=2,color="#9f35ff",label="log2(x)")
	#
	# y3=[math.log(a,3) for a in x]
	# plt.plot(x,y3,linewidth=2,color="#f75000",label="log3(x)")
	#
	# plt.legend(loc="lower right")
	# plt.grid(True)
	# plt.show()





	# t = time()
	# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# listb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01]
	# x = 0
	# for i in range(1000000):# range效率比xrange效率低,使用xrange代替
	# 	for a in range(len(lista)):# len(lista)在循环内重复计算,提到最外层
	# 		for b in range(len(listb)):# len(listb)在循环内重复计算,提到最外层
	# 			x = x + lista[a] + listb[b]# lista[a]在循环内重复计算,提到lista的循环
	# print x
	# print "total run time:"
	# print time() - t
	# 20.4489998817

	# t = time()
	# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	# listb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01]
	# x = 0
	# len1 = len(lista)
	# len2 = len(listb)
	# for i in xrange(1000000):
	# 	for a in xrange(len1):
	# 		temp = lista[a]
	# 		for b in xrange(len2):
	# 			x = x + temp + listb[b]
	# print x
	# print "total run time:"
	# print time() - t
	# # 17.7350001335


	# t = time()
	# list = ['a', 'b', 'is', 'python', 'jason', 'hello', 'hill', 'with', 'phone', 'test', 'dfdf', 'apple', 'pddf', 'ind',
	# 		'basic', 'none', 'baecr', 'var', 'bana', 'dd', 'wrd']
	# total = []
	# for i in range(1000000):
	# 	for w in list:
	# 		total.append(w)
	# print "total run time:"
	# print time() - t
	# 2.52800011635

	# t = time()
	# list = ['a', 'b', 'is', 'python', 'jason', 'hello', 'hill', 'with', 'phone', 'test', 'dfdf', 'apple', 'pddf', 'ind',
	# 		'basic', 'none', 'baecr', 'var', 'bana', 'dd', 'wrd']
	# total = []
	# for i in range(1000000):
	# 	a = [w for w in list]#使用列表生成式
	# 	total.extend(a)
	# print "total run time:"
	# print time() - t
	#2.02600002289

	t = time()
	list = ['a', 'b', 'is', 'python', 'jason', 'hello', 'hill', 'with', 'phone', 'test', 'dfdf', 'apple', 'pddf', 'ind',
			'basic', 'none', 'baecr', 'var', 'bana', 'dd', 'wrd']
	total = []
	for i in range(1000000):
		a = (w for w in list)#使用生成器
		total.extend(a)
	print "total run time:"
	print time() - t
	#1.84500002861