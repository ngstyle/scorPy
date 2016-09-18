# -- coding: utf-8 --

from collections import Iterable
from collections import Iterator

# 集合数据类型，如list、tuple、dict、set、str等；
# generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。


for x in [1,2,3,4,5]:
	print('value:',x)

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# for 循环等价于下边：
it = iter([1,2,3,4,5])
while True:
	try:
		value = next(it)
		print('result:',value)
	except StopIteration as e:
		breakf