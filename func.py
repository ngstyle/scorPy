# -*- coding: utf-8 -*-
# 函数调用 (注意参数个数以及参数类型的传入)
print(abs(-100))
print('max num:',max(3,5,2,8,4))

n1 = 255
print('str:',str(n1))
print('hex:',hex(n1))


def my_abs(x):
	# 参数类型检查
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if (x > 0):
		return x
	else:
		return -x

print('自定义 func:',my_abs(-100))

# pass语句什么都不做,可作为占位符
def nop():
	pass

print('do nothing',nop())


# 导入math包 
import math

# 返回多个参数，其实就是tuple
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

print(move(100,100,60,math.pi/6))

# 默认参数
# 默认参数(可变对象)的坑（http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000）
def encroll(name,gender,age=25,city='sz'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)

encroll('chon','F')


# 可变参数 *numbers
def calc(*numbers):
	sum = 0
	for num in numbers:
		sum += num * num
	return sum

print('sum =',calc(1,2,3))

# 已有list或者tuple，可在前边加* 作为参数传入
nums = [1,2,3,4]
print('sum1 =',calc(*nums))


# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:',name,'age:',age,'other:',kw)

person('chon',25,city='sz',job='Engineer')

# 同上，当我们有了一个dict时，可以加两个*转成关键字参数
extra = {'city': 'Luoyang', 'job': 'Engineer','address': 'baoan'}
person('vivian',24,**extra)


# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def anotherPerson(name,age,*,city,job):
	print(name,age,city,job)

extra = {'city': 'Luoyang', 'job': 'Engineer'}
anotherPerson('vivian',24,**extra)

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了

# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)

# 命名关键字参数可以有缺省值，从而简化调用：
# def person(name, age, *, city='Beijing', job):
#     print(name, age, city, job)

# person('Jack', 24, job='Engineer')

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


# 小结
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。









