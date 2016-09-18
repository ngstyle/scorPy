# -- coding: utf-8 --
from collections import Iterable

d = {'a':1,'b':2,'c':3}

for key in d:
	print('key:',key)
	print('value:',d[key])

for value in d.values():
	print('v:',value)

for k,v in d.items():
	print(k,v)

print('是否可迭代：',isinstance(d,Iterable))


# 如果要对list实现类似Java那样的下标循环，内置的enumerate函数可以把一个list变成索引-元素对
for i,value in enumerate(['A','B','C']):
	print(i,value)

# 遍历dict，还是遍历的key
for i,key in enumerate(d):
	print(i,key)

# for x, y in [(1, 1), (2, 4), (3,9)]:
# 	print(x, y)