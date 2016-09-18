#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('name = %s,score = %s' % (self.__name,self.__score))

	def get_score(self):
		return self.__score

	def set_score(self,score):
		self.__score = score

	def get_name(self):
		return self.__name

vivian = Student('Vivian',98)
chon = Student('Chon',87)

vivian.print_score()
chon.print_score()

# 双下划线开头的实例变量是不是一定不能从外部访问呢？
# 其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量：
# print(chon._Student__name)

chon.__name = '__chon'

# 表面上看，外部代码“成功”地设置了__name变量，
# 但实际上这个__name变量和class内部的__name变量不是一个变量！
# 内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。
print(chon.__name)			
print(chon.get_name())


# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：