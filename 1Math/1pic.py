#!/usr/bin/python
# -*- coding:utf-8 -*-

import math
import matplotlib.pylab as plt

if __name__ == '__main__':
	x = [float(i) / 100.0 for i in range(1, 300)]
	y = [math.log(i) for i in x]
	# 红线
	plt.plot(x,y,"r-",linewidth=3,label="log Curve")

	a=[x[20],x[175]]
	b=[y[20],y[175]]
	# 绿线
	plt.plot(a,b,"g-",linewidth=2)
	# 星星
	plt.plot(a,b,"b*",markersize=15,alpha=0.75)
	plt.legend(loc="upper left")
	# 图像中间是否用虚线
	plt.grid(True)

	plt.xlabel("x")
	plt.ylabel("log(x)")
	plt.show()



