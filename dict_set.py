# -*- coding: utf-8 -*-
# dict & set

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# 需要牢记的第一条就是dict的key必须是不可变对象。

d = {'Michanel': 60,'Bob': 98,'chon':87}

# 可以追加
d['vivian'] = 99
d['冲'] = 100

print(d)

# key 不存在时会报错，可给默认值如果不存在(get 方法)
# print(d['ryoka'])
print(d.get('ryoka','default'))

# 重复赋值会冲掉之前赋值的值
d['冲'] = 55
print(d)


# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

# 要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3,4])
s.add(5)
# 重复添加无效
s.add(3)

# 添加tuple
s.add((1,2,3))
# 添加不可变元素，tuple中有list时出错
# s.add((1,[2,3]))

s.remove(2)

print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,2,4])
s2 = set([2,3,4])

ands = s1 & s2
print(ands)

ors = s1 | s2
print(ors)





