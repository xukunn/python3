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
