# list & tuple
# -*- coding: utf-8 -*-
L = [1,222,3,45]
T = (3,4,6,3,2)

classmates = ['Michale','Bob','Robin']

print(L)
print(T)
print(classmates)


L.append(1000)
L.insert(0,-1)

# 排序
L.sort()
L.pop(1)

print(L)
# 数组最后一个元素
print(classmates[-1])	


bmi = 80.5 / 1.75 / 1.75
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
	print('肥胖')
else:
	print('严重肥胖')

print(list(range(5)))

sum = 0
for value in range(101):
	sum += value
print("sum =",sum)

sum = 0
n = 100
while n > 0:
	sum += n
	n -= 1
print('sum =',sum)

for name in classmates:
	print('Hello,',name)







