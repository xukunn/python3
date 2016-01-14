#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 面向对象基础 '

__author__ = 'xukunn'

import sys
import functools


# 动态语言的鸭子模型,多态不一定必须是继承,可以一个类有多态类的方法即可.

class Animal(object):
	def __init__(self, name, age):
		if isinstance(age, int):
			self.name = name
			self.__age = age
		else:
			raise ValueError('age must be int')

	def run(self):
		print('animal run')

	def get_age(self):
		return self.__age


class Dog(Animal):
	pass


class Cat(object):
	def run(self):
		print('cat run')


d = Dog('dod', 10)
d.run()

cat = Cat()
cat.run()

print(dir(d))
print(type(d))
print(isinstance(d, (Dog, Animal)))  # 可以一个,可以多个
import types

print(type(123) == int)  # 判断是否是整形
print(type(abs) == types.BuiltinFunctionType)  # 判断是否是函数类型

# 面向对象高级编程

