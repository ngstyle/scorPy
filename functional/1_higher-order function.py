# -- coding: utf-8 --

# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。


# 函数本身也可以赋值给变量，即：变量可以指向函数。可通过该变量来调用这个函数
f = abs
print(f(-100))

# 函数名也是变量
# abs = 10
# abs(-10)

# 把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！

# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x,y,f):
	return f(x) + f(y)

print(add(2,-9,abs))


from math import sqrt
def same(x,*fs):
    s=[f(x) for f in fs]
    return s
print(same(2,sqrt,abs))

# Python内建了map()和reduce()函数

def f(x):
	return x*x

r = map(f,[1,2,3,4,5])
print(list(r))
print([x*x for x in [1,2,3,4,5]])



# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def add(x,y):
	return x + y

print(reduce(add,[1,3,5,7,9]))

def fn(x,y):
	return x * 10 + y

print(reduce(fn,[1,3,5,7,9]))

def str2int(s):
	def fn(x,y):
		return x * 10 + y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	return reduce(fn,map(char2num,s))

print(str2int('456789'))

# 变成首字母大写，其他小写
names = ['adam', 'LISA', 'barT']

# def normalize(name):
# 	return name.capitalize()

def normalize(name):
	return name[0].upper() + name[1:].lower()

print(list(map(normalize,names)))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(L):
	return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

# def str2float(s):
# 	def char2num(s):
# 		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
# 	def f1(x,y):
# 		return x*10 + y
# 	def f2(x,y):
# 		return x/10 + y

# 	s = s.split('.')
# 	integer = reduce(f1,map(char2num,s[0]))
# 	decimal = reduce(f2,map(char2num,s[1][::-1]))
# 	return integer + decimal / 10

# print(str2float('123.456'))

def str2float(s):
    arrays = s.split('.')
    str = arrays[0] + arrays[1]
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return (reduce(lambda x, y: x * 10 + y, map(char2num, str)))/pow(10,len(arrays[1]))

print('str2float(\'123.456\') =', str2float('123.456'))


# ------------------------------------------------------------------------------------------------
# Python内建的filter()函数用于过滤序列。

def is_odd(n):
	return n % 2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6,7])))

def no_empty(s):
	return s and s.strip()

print(list(filter(no_empty,['a',None,'','b','  '])))


# 计算素数的一个方法是埃氏筛法
# 首先构造一个奇数序列
def _odd_iter():
	n = 1
	while True:
		n += 2
		yield n

# 然后定义一个筛选函数(不能被n整除)：
def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter()  # 初始化序列
	while True:
		n = next(it)  # 返回序列第一个
		yield n
		it = filter(_not_divisible(n),it)

for n in primes():
	if n < 100:
		print(n)
	else:
		break

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。利用filter()滤掉非回数：
# def is_palindrome(n):
# 	s = str(n)

# 	i = 0
# 	while i < len(s) / 2:
# 		if s[i] != s[len(s) - 1 -i]:
# 			return False
# 		i += 1

# 	return True

def is_palindrome(n):
	return n == int(str(n)[::-1])

output = filter(is_palindrome, range(1, 1000))
print(list(output))


# 排序
print(sorted([36, 5, -12, 9, -21]))
# 按绝对值大小进行排序
print(sorted([36, 5, -12, 9, -21],key=abs))

# 高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。
# ['bob', 'about', 'Zoo', 'Credit']
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))

# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=lambda t:t[0].upper()))

# 命名关键字参数
print(sorted(L,key=lambda t:t[1],reverse=True))
print(sorted(L,**{'key':lambda t:t[1],'reverse':True}))

