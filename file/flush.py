
#coding=utf-8
import sys


fd = open('file1.txt','a+')

while True:

    s = sys.stdin.readline()
    # if s == '\n':
    #     break
    fd.write(s)
    fd.flush()  # 手动刷新缓冲
