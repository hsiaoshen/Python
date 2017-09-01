#coding=utf-8

# 几个内建函数的使用 issubclass,isinstance,hasattr,getattr,setattr,delattr

class A(object):
     attr = "test"

class B(A):
    pass

class C(B):
    pass

c = C()

print issubclass(C,A)   # 判断是否有继承关系

print isinstance(c,(A,B,C)) # 判断对象是不是继承了那些类,多个类时用元组包含

print isinstance('hello',int) #判断是不是属于某个类型

print "=================================="

print hasattr(c,"attr") #判断对象中是否有该属性

print getattr(c, 'attr') # 获取c中attr的值,若没有会报错

print getattr(c, 'att','k') #若是第三个参数存在,没有该属性但是会给该属性赋值为最后的参数

setattr(c,'name','zhansan')  # 可以来给c设置属性的,相当于 c.name = 'zhansan'

print c.name