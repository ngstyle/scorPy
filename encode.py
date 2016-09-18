
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：'中文'.encode('utf-8')
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
# 例如：b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

print(ord('A'))
print(chr(25991))

str = 'ABC'.encode('ascii')
print(str)


print('\'中文\'占',len('中文'),'字符')
print('\'中文\'占U8编码',len('中文'.encode('utf-8')),'字节')

print('decode:',b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 格式化的字符串的输出
print('My name is %s,age is %d' % ('chon',25))

# %用%%转意
print('growth rate: %d%%' % 7)

# exercise
s1 = 72
s2 = 85
r = (s2 - s1)/s1 * 100
print('提升了 %.1f%%' % r)