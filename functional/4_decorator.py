# -- coding: utf-8 --

# def now():
# 	print('2016-09-12 18:02:22')

# print(now.__name__)

# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

# 本质上，decorator就是一个返回函数的高阶函数。

import functools

def log(func):
	def wrapper(*args,**kw):
		print('call %s()' % func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def now():
	print('2016-09-12 18:24:03')

now()



def log2(text):
	def decorate(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s call %s()' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorate

@log2('chon')
def now2():
	print('2016-09-12 20:54:58')

now2() # now2 = log2('chon')(now)

print(now2.__name__)  # wrapper or now2


# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
# OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，
# 直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。


# exercise
def logger(args_or_func):
	def decorate(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('begin call %s() %s' % (func.__name__,args_or_func))
			result = func(*args,**kw)
			print('end call!!!')
			return result
		return wrapper
	return decorate(args_or_func) if callable(args_or_func) else decorate

@logger('kakak')
def test():
	print('test func body!')

test()



# 其实很简单，用参数来记忆

# 最里层：参数一定是*args, **kw，一定会在函数内调用func(*args, **kw)
# 次里层：参数一定是func，当然你可以用其他名字命名，但是这参数一定是函数，而且会在最里层调用func(*args, **kw)
# 最外层：如果装饰器是不需要带参数的，那次里层也是最外层了，最外层的函数名就是装饰器名称，否则还需要包装多一层去接收装饰器的参数。
# 装饰器是否带参数决定一个装饰器是两层还是三层（再多就没必要了），但是最里层和次里层的参数都是确定的。









