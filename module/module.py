#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块的文档注释
'a test module'

__author__ = 'chon'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello,World!')
	elif len(args) == 2:
		print('Hello,%s!' % (args[1]))
	else:
		print('There are many args!')

if __name__ == '__main__':
	test()
	print(__doc__)

# _开头命名的变量或者函数私有，约定
def _private1(name):
	print('Hello,%s' % (name))

def _private2(name):
	print('Hi,%s' % (name))

def greeting(name):
	if len(name) > 3:
		_private1(name)
	else:
		_private2(name)

greeting('chon')
greeting('vv')


# 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
# 在Python中，安装第三方模块，是通过包管理工具pip完成的。

# pip install Pillow
from PIL import Image

print('path:',sys.path)
im = Image.open('vivian.jpg')
print(im.format,im.size,im.mode)



