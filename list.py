#!/usr/bin/python
# -*- coding: utf-8 -*-

data = []
print(type(data)) # <type 'list'>
print(len(data)) # 0

data.append(1)
data.append(2)
data.append(3)
data.append(4)
data.append(5)
print(len(data)) # 5
print(data) # [1, 2, 3, 4, 5]
del data[0]
print(data) # [2, 3, 4, 5]
del data[1]
print(data) # [2, 4, 5]

data2 = [1, 2, 3]
print(len(data2)) # 3
print(data2) # [1, 2, 3]
