#coding=utf-8
import time

line1 = 0

fd = open('test.txt','a+')

for line in fd:
    line1 += 1
# print line1 


while True:
    line1 += 1
    time1 = time.strftime("%Y-%m-%d %X", time.localtime())
    print >> fd,('%d,' + time1)%(line1)
    fd.flush()   #手动刷新缓冲区
    time.sleep(1)

