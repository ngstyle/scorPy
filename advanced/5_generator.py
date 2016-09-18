# -- coding:utf-8 --
# generator 生成器

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x*x for x in range(10)]
G = (x*x for x in range(10))

print('L',L)
print('G',G)

# 打印G中的值
print(next(G))
print(next(G))

for n in G:
	print('value:',n)

# 斐波拉契数列
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		# print(b)
		yield b
		a,b = b,a+b
		n += 1
	return 'done'

# fib(10)
f = fib(6)
# for n in f:
# 	print('result:',n)

# 获取generator返回值
while True:
	try:
		x = next(f)
		print('value:',	x)
	except StopIteration as e:
		print('Generator return value is',e.value)
		break


def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield 2
	print('step 3')
	yield 3

# 获取generator 遍历
o = odd()
for i in o:
	print('value:',i)


# 杨辉三角 列表生成
def triangles(max):
    L = [1]
    n = 0
    while n < max:
        yield L
        L.append(0);
        L = [L[i-1] + L[i] for i in range(len(L))]
        n += 1


t = triangles(10)

for tt in t:
	print(tt)





