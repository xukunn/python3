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

class Student(object):
	__slots__ = ('name', 'age')  # 限制动态添加属性,仅对当前类有效,继承的子类不起作用


# 动态添加方法

def set_age(self, age):
	self.age = age


from types import MethodType

Student.set_age = MethodType(set_age, Student)

stu = Student()
stu.set_age(34)
print(stu.age)
stu.name = 'jack'


# stu.score = 98  # 没有这个属性


# @property

class Teacher(object):
	@property
	def birth(self):
		return self._birth  # 注意这里的_,不能和方法名相同  否者就成了无限递归了  self.birth调用的是方法

	@birth.setter  # 可写属性
	def birth(self, value):
		self._birth = value

	@property  # 只读属性
	def age(self):
		return 2016 - self._birth


tea = Teacher()
tea.birth = 1989  # 调用的是set_birth()方法,而不是直接读取属性
# tea.age = 20  # 不能设置该属性


# 多继承 MixIn
class Flyable(object):
	def fly(self):
		print('flying...')


class Bird(Animal,Flyable):
	pass


b = Bird('bb',23)
b.run()
b.fly()