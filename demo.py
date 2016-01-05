#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

'''
1. 输入输出,print用,连接
'''

name = input('please input your name: ')
print('hello,',name)

#除法
>>> 10/3
3.3333333333333335
>>> 10//3 #地板除
3
>>> 10%3
1

#字符串
>>> '总问'.encode('utf-8')
b'\xe6\x80\xbb\xe9\x97\xae'#b开头的表示字符集合bytes

>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
#字符串长度和bytes长度len()
>>> len('中文')
2
>>> len('中文'.encode('utf-8'))
6
#占位符%
字符串:%s
>>> 'hello,%s' % 'world'#一个占位括号()可以省略
'hello,world'
>>> 'hello,%s 和 %s' % ('tom','jerry')
'hello,tom 和 jerry'
>>> '%.2f' % 3.1415926   #两位小数的格式
'3.14'

