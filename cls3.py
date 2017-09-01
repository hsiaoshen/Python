#coding=utf-8

# 添加特有方法:记得若是定义一个方法,必须有形参self,定义一个函数就不需要了


class ClsM(object):
    name = 'lisi'
    def __init__(self):
        print 'sunquan'
    
#1:这种方法是给类中添加方法

def fun(self):
    print 'add function'

ClsM.fun = fun

a = ClsM()

print a.name

a.fun()

#2:给对象添加特有方法需要传参

def fun1(self):
    print 'add fun1'

a.f = fun1

a.f(1)

#3: 给对象添加特有方法,特有方法的不需要传参

def fun2(self):
    print 'add fun2'

import new

a.f = new.instancemethod(fun2,a,ClsM)

a.f()