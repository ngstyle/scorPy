#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(type(123))
print(type('str'))

print(type(11) == int)

import types

def fn():
	pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


class Animal(object):

	def run(self):
		print('Animal is running...')


class Dog(Animal):

	def run(self):
		print('Dog is running...')


dog = Dog()
dog.run()

# isinstance 判断类型
print(isinstance(dog,Animal))


# 可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1,2,3.4],(list,tuple)))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir('abc'))

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态

print(hasattr(dog,'run'))
print(getattr(dog,'run'))
# print(getattr(dog,'eat'))

setattr(dog,'age',2)
print(hasattr(dog,'age'))
print(getattr(dog,'age'))

# 实例属性和类属性

class Computer(object):
	type = 'mac'

	def __init__(self,size):
		self.__size = size

# 类属性
print(Computer.type)

computer = Computer(19)
print(computer.type)

# 设置实例对象的type属性
computer.type = 'mbp'
print(computer.type)

# 删除实例对象的type属性
del computer.type
print(computer.type)










