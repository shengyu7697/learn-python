#!/usr/bin/python
# -*- coding: utf-8 -*-

print('開檔，並覆寫')
f = open('output.txt', 'w')
f.write('123')
f.write('456\n')
f.close

print('開檔，並新增內容')
f = open('output.txt', 'a+')
f.write('123')
f.write('456\n')

print('移動指針, 讀出數值')
f.seek(5)
print(f.read(1))
f.close
