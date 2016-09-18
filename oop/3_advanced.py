#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'多重继承、定制类、元类'

# 给实例动态添加属性和方法
class Student(object):
	pass

s = Student()
# 动态添加属性
s.name = 'chon'
print(s.name)

from types import MethodType

def set_age(self,age):
	self.age = age

# 动态给实例添加方法，但是只针对当前实例，创建其他实例时并没有set_age方法
# 可添加类方法，各实例均可调用
s.set_age = MethodType(set_age,s)
s.set_age(24)

print('age:',s.age)

# 可添加类方法
# def set_score(self, score):
# 	self.score = score

# Student.set_score = set_score


# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class GraduateStudent(object):
	__slots__ = ('age','name')


g = GraduateStudent()
g.age = 26
g.name = 'vivian'
# g.score = 96     # score 不在__slots__定义的tuple中，会报错			


class Person(object):

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self,age):
		if not isinstance(age,int):
			raise ValueError('age must be an integer!')
		if age < 0:
			raise ValueError('age must older than 0')
		self._age = age

p = Person()
p.age = 25
print('Person age:',p.age)


class Screen(object):
	@property
	def width(self):
		return self._width
	
	@width.setter
	def width(self,width):
		self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self,height):
		self._height = height

	@property
	def resolution(self):
		return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
	
# python多重继承

# 定制类
# __slots__ __len__ __str__ __repr__ __iter__ __getitem__ __getattr__ __call__


class Chain(object):
	def __init__(self,path=''):
		self._path = path

	def __getattr__(self,path):
		return Chain(('%s/%s' % (self._path,path)))

	def __str__(self):
		return self._path

	def __call__(self,path):
		return Chain('%s/%s' % (self._path,path))

	__repr__ = __str__


print(Chain().user('chon').timeline.list)





