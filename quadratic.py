# -*- coding: utf-8 -*-
import math

def quadratic(a,b,c):
	if not isinstance(a,(int,float)):
		raise TypeError('bad operand type: wrong number \'a\'',a)
	if not isinstance(b,(int,float)):
		raise TypeError('bad operand type: wrong number \'b\'',b)
	if not isinstance(c,(int,float)):
		raise TypeError('bad operand type: wrong number \'c\'',c)

	x1 = None
	x2 = None
	delta = b * b - 4 * a * c
	if delta == 0:
		x1 = -b / (2 * a)
		x2 = -b / (2 * a)
	elif delta > 0:
		x1 = (-b + math.sqrt(delta)) / (2 * a)
		x2 = (-b - math.sqrt(delta)) / (2 * a)
	return x1,x2

print(quadratic(2,3,1))