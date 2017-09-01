#coding=utf-8

# python3中

def f(a,*b, c):
    print (a,b,c)

# f(1,2,3,4)  这赋值是错误的

f(1,2,3,c=5)
