#!/usr/bin/env python3
# -*- coding: utf-8 -*-

函数


>>> int(2.9)
2
>>> round(25.5)
26
>>> float('2.34')
2.34
>>> str(1.23)
'1.23'
>>> bool('')
False

#自定义函数
def myAbs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad arg type')
	if x>=0:
		return x
	else:
		return -x

#空函数 pass
def functionA():
	pass  #占位用  也可以用在if/else中

if age >= 18:
    pass

#返回多个值:其实是返回一个tuple ,只是省略了括号()

#导包
import math

#多次方函数  
def power(x,n = 2): # 默认参数要用不变对象 如str None 数字 
	y = 1
	for i in range(n):
		y  = y*x
	return y

#可变参数
def sumPower(*numbers):
	sum = 0
	for n in numbers:
		sum = sum +n*n

	return sum
#如果已经有一个list了,可以用*list传入
>>> nums = [1,2,3]
>>> sumPower(*nums)
14

#关键字参数  **kw   随意传入dict
def person(name,age,**kw):
	print(name,'is',age,'years.',kw)

>>> person('jack',34,city='beijing')
jack is 34 years. {'city': 'beijing'}
>>> kw = {'city':'beijing','sexy':'yes'}
>>> person('jack',34,**kw)
jack is 34 years. {'sexy': 'yes', 'city': 'beijing'}

#命名关键字参数
def person(name,*,age,city = '北京'):  #*是特殊分隔符不是参数
	print(name,'is',age,'years.',city)

>>> person('jack',age = 34)
jack is 34 years. 北京

#任意函数都能这样调用:func(*args, **kw) *args是可变参数，args接收的是一个tuple；**kw是关键字参数，kw接收的是一个dict。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

#递归函数(尾递归优化)
def jiechen(n,last=1):
	if n == 1:
		return last
	return jiechen(n-1,n*last)

	