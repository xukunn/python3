#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

#函数式编程

#函数名也是变量
a = abs
#编写高阶函数，就是让函数的参数能够接收别的函数。

def add(x,y,f):
	return f(x)+f(y)

>>> add(-2,-5,abs)
7
#map/reduce
map()返回的是Iterator,需要用list()把整个序列的next()都弄出来
>>> list(map(str,[1,2,3,23]))
['1', '2', '3', '23']
>>> from functools import reduce
>>> reduce(lambda x,y:x*10+y,[1,2,3])
123

#str转int
def str2int(s):

	def char2int(s):
		return {'0':0,'1':1,'2':2,'3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

	return reduce( lambda x,y:x*10+y, map(char2int,s))

>>> str2int('192359126')
192359126

#练习1,字符串首字母大写
1,复杂
def normalize(name):
	normal =''
	for i,x in enumerate(name):
		if i == 0:
			x = x.upper()
		else:
			x = x.lower()

		normal = normal + x
	return normal
2,利用切片
def normalize(name):
	return name[0].upper()+name[1:].lower();