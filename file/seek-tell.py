#coding=utf-8
import os

# fd.tell():偏移量
# fd.seek(offset[,0/1/2])
# 0:起始位置   1:当前位置    2:结尾

fd = open('file1.txt','r+')

print fd.tell()

fd.read(12)

print fd.tell()

a = fd.read(24)

print fd.tell()

fd.seek(0,1)

fd.write('案发生地方')




fd.close()