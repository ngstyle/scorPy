# -- coding: utf-8 --
# comprehensions 列表生成式

# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：

# 生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
print([x*x for x in range(1,11)])
print((map(lambda x:x*x,range(1,11))))

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x*x for x in range(1,11) if x%2 == 0])


# 两层循环，可以生成全排列：
print([m + n for m in 'chon' for n in 'vivian'])


import os
# 列出当前目录的文件名和目录名
print([d for d in os.listdir('.')])


d = {'x': 'X','y':'Y','z':'Z'}
print([k + '=' + v for k,v in d.items()])

L = ['Hello', 'World', 24,'IBM', 'Apple']
print([s.lower() for s in L if isinstance(s,str)])