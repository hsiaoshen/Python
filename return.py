#coding=utf-8

# 函数中return若没返回值结果为None,若返回多个值用一个变量来接收,结果为一个元组

def fun():
    return

def fun1():
    return 1,2,3,4

k =  fun()
r = fun1()
a,b,c,d = fun1()
print k,r,a,b,c,d