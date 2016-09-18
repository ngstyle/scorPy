# -- coding: utf-8 --
# 切片 取一个list或tuple的部分元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 从索引0开始取，直到索引3为止，但不包括索引3
print(L[:3])


arr = list(range(101))

# 取前十
print(arr[:10])
# 取倒数十
print(arr[-10:])
# 4 - 20每两个取一个（不包括20）
print(arr[4:20:2])
# 20 - 4每两个取一个（不包括4）
print(arr[20:4:-2])
# 每5个取一个
print(arr[::5])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符

print('chon&vivian'[::2])