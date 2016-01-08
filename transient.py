#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

#杨辉三角
def yanghui(n):
	l = [1]
	while n>0:
		yield l
		l = [1]+[l[index]+l[index+1] for index  in range(len(l)-1)] +[1]
		n = n-1







	

