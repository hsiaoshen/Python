#coding=utf-8
 
# fd 是文件描述符,一个进程最多可以打开1204个fd,系统默认打开3个

fd  = open('file.txt')

# str1  = fd.read()
# str2 = fd.read(128)

# s  =  fd.readlines()   # 一次读取一行,返回一个列表

# print s   # 打印出来的是一个列表
# print s[0]  # 如果是中文这个打印出的是内容

for line in fd:
    print line,

fd.close()   # 打开就要关闭

# print fd

# with的好处是,代码块执行完自动清除
# with open('file.txt') as fd:
#    pass


import sys

# print sys.stdin

# print sys.stdin.readline()
