#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce



def normalize(name):
	return name[0].upper()+name[1:].lower();

def prod(L):
	return reduce(lambda x,y:x*y ,L)

def str2float(s):
	s1,s2 = s.split('.')
	









	

