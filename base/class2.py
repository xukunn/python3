#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 高级面向对象'

__author__ = 'xukunn'

import sys
import functools


class Student(object):
	def __init__(self, name):
		self._name = name

	def __str__(self):
		return 'Student:' + self._name

	__repr__ = __str__  # repr调试用


stu = Student('lily')
print(stu)
stu

# 枚举
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


@unique
class Weekday(Enum):
	Sun = 0  # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6


print(Weekday.Fri)
print(Month(2))


# type() 动态创建class

def fn(self, name='world'):
	print('hello,', name)


Hello = type('Hello', (object,), dict(sayHello=fn))  # 创建Hello class 有个方法sayHello

h = Hello()
h.sayHello()

# 元类  metaclass
'''当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。'''
