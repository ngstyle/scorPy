# -- coding: utf-8 --

import functools

# 二进制转成十进制
def int2(str,base=2):
	return int(str,base)

print(int2('10000'))


# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义intp2()
intp2 = functools.partial(int,base=2)
print(intp2('1111'))


# 实际上会把10作为*args的一部分自动加到左边
max2 = functools.partial(max,10)
print(max2(5,3,9,6))