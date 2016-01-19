#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 进程线程 '

__author__ = 'xukunn'

import sys
import functools

import os

# print("Process: ",os.getpid(),os.getppid())
#
# print(os.fork())
# print(os.getpid(),os.getppid())

from multiprocessing import Process


# 子进程将要执行的代码
def run_proc(name):
	print(os.getpid(), 'running', '父进程:', os.getppid(), '参数:', name)


if __name__ == '__main__':
	print('父进程:', os.getpid())
	p = Process(target=run_proc, args=('jack',))
	print('子进程要开始了...')
	p.start()
	p.join()
	print('子进程完成了')

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('exit code', r)

# 进程间通讯
from multiprocessing import Process, Queue
import time, random


# 写数据
def write(q):
	print(os.getpid(), '----write-----')
	for value in ['A', 'B', 'c']:
		print(value, '--->queue')
		q.put(value)
		time.sleep(random.random())


# 读数据
def read(q):
	print(os.getpid(), '----read----')
	while True:
		value = q.get(True)
		print(value, '<----')


if __name__ == '__main__':
	# 父进程创建queue,并传给子进程
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pr.start()
	pw.join()  # 等待pw结束
	pr.terminate()  # 读是一个死循环,强行停止

# 线程
import threading


def loop():
	print(threading.current_thread().name, 'running')
	for n in range(5):
		print(threading.current_thread().name, ':', n)
		time.sleep(1)
	print(threading.current_thread().name, 'end....')


print(threading.current_thread().name, 'running...')
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print(threading.current_thread().name, 'ended')

'''多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
'''

import threading, multiprocessing

print(multiprocessing.cpu_count())

'''现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操作系统提供的异步IO支持，
就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，
Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。在多核CPU上，
可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。
用异步IO编程模型来实现多任务是一个主要的趋势。

对应到Python语言，单进程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。
'''

#threadlocal

local_school = threading.local()

def process_student():
	std = local_school.student
	print('hello',std)

def process_thread(name):
	local_school.student = name
	process_student()


t1 = threading.Thread(target=process_thread,args=('jack',),name='thread1')
t2 = threading.Thread(target=process_thread,args=('lily',),name='thread2')
t1.start()
t2.start()
t1.join()
t2.join()
