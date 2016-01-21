#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' io '

__author__ = 'xukunn'

import sys
import functools

with open('./base.py', 'r') as f:
	print(f.read())

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

import os
print(os.path.abspath('.'))

l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(l)

