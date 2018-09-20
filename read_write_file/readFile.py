#!/usr/bin/python
# -*- coding: utf-8 -*-

print('一次讀全部')
f = open('input.txt')
print(f.read())
f.close

print('一次讀一行')
f = open('input.txt')
for line in f.readlines():
	print(line)
f.close
