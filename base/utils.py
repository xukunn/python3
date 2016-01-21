# 时间 datetime
from datetime import datetime

now = datetime.now()
print(now)
print(now.timestamp())
print(now.strftime('%a,%b %d %H:%M'))

time = '2015-1-21 9:01:30'
cday = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
print(cday)
print(cday.timestamp())

# collections

# 表示一个点
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(isinstance(p,tuple))

# deque  双向链表,增删快
from collections import deque
q = deque(['a','b','c'])
q.append('d')
q.appendleft('X')
print(q)
q.pop()
print(q)
q.popleft()
print(q)

# counter 计数器
from collections import  Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch]+1

print(c)

# 有序的dict:按照添加的顺序

from collections import OrderedDict
od = OrderedDict()
od['z'] = 1
od['a'] = 2
od['b'] = 3
print(list(od.keys()))

