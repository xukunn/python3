#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 基础模块 主要是前两行的注释 '

__author__ = 'xukunn'

import sys
import functools


def test():
	pass


if __name__ == '__main__':
	test()

# 作用域: _开头的是私有的
_name = 'xk'


# 私有函数
def _test():
	pass


_test()

print(sys.path)
