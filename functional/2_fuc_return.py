# -- coding: utf-8 --

def calc_sum(*args):
	sum = 0
	for arg in args:
		sum += arg
	return sum

print('sum =',calc_sum(1,2,3,4))

# 不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
	def calc_sum():
		sum = 0
		for arg in args:
			sum += arg
		return sum

	return calc_sum

print(lazy_sum(1,2,3,4))
print(lazy_sum(1,2,3)())

f1 = lazy_sum(1,2,3)
f2 = lazy_sum(1,2,3)
print(f1 == f2)    #False

# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数calc_sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

# f1 f2 f3与数组中元素一一对应
f1, f2, f3 = count()

print(f1())
print(f2())

# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count2():
	def f(j):
		def g():
			return j*j
		return g

	fs = []
	for i in range(1,4):
		fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
	return fs

f3,f4,f5 = count2()
print(f3())
print(f4())

