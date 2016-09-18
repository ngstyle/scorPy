#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello python')

def normalize(name):
	return name.capitalize()

L1 = ['adam','LISA','barT']
L2 = list(map(normalize,L1))
print(L2)

print('100 + 200 =',100+200)

# stdinput,阻塞式
name = input('Please input your name:\n')
print('Hello',name)