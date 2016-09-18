#!usr/bin/env python3
# -*- coding: utf-8 -*-

'枚举'

__author__ = 'chon'

from enum import Enum

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))


for name,member in Month.__members__.items():
	print(name, '==>',member,member.value)