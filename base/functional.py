#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

'''
函数式编程
'''


# 求和函数
def lazy_sum(*args):
	def sum():
		all = 0
		for n in args:
			all = all + n
		return all

	return sum


f = lazy_sum(1, 2, 3, 4)
print(f())  # 10   注意 f 和f()的区别


# 闭包
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量


# 匿名函数lambda
def build(x, y):
	return lambda: x * x + y * y  # 返回的是一个函数


print(build(2, 3)())

print(abs.__name__)  # 函数的属性

# 偏函数  固定住函数的参数,返回一个新的函数
import functools

int2 = functools.partial(int, base=2)  # 默认base是10
print(int2('1001'))  # 9


# 装饰器

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print("call")
		return func(*args, **kw)

	return wrapper


@log  # now = log(now)
def now():
	print('2016')


now()
print(now.__name__)


# 完善的log
def log(text='log'):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print(text,':', func.__name__)
			r = func(*args, **kw)
			print('endcall',':', func.__name__)
			return r

		return wrapper

	return decorator


@log('hehe')
def now():
	print('2017')

@log()
def lastYear():
	print('2015')

now()
lastYear()
