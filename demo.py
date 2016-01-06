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

#list 和  tuple(元素不可变)
>>> names = ['lily','hongyang','jack']
>>> names
['lily', 'hongyang', 'jack']
>>> names[-1] 
'jack'   #-1表示倒数第几个    
>>> names[len(names)-1]
'jack'
>>> list =[]
>>> len(list)
0
#缺陷:tuple
>>> t = (1)    //()表示运算中的小括号
>>> t
1
>>> t = (1,) 
>>> t
(1,)
#if elif else 注意缩进
>>> if age<6:
...     print('<6')
... elif age<9:
...     print('<9')
... else:
...     print('18')
... 
18
#循环for x in ()        
>>> sum = 0
>>> for x in range(101):
...     sum = sum+x
... 
>>> print(sum)
5050
#while  true
>>> n =1
>>> sum = 0
>>> while n<100:
...     sum = sum +n
...     n = n+1
... 
>>> print(sum)
4950
#dict 相当于java中map
>>> students = {'jack':21,'bob':18,'lily':19}
>>> students['jack']
21
>>> students['heh'] = 88   #增改
>>> 'tom' in students
False
>>> students.get('jack')
21   #不存在会返回None
>>> students.pop('jack')   #删除
21
#set  无序,无重复
>>> s = set([1,3,2,3])   #传入一个list
>>> s
{1, 2, 3}
>>> s.add(4)
>>> s.remove(1)
>>> s
{2, 3, 4}

