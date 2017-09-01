#coding=utf-8

# 对象方法,类方法和静态方法:都可以类或者对象调用,但是传入参数不同


# 传入的是实例化的对象:self等同于a对象
class A(object):
    name = '1'
    def fun(self):
        print '对象方法'

a =A()

a.fun()


# staticmethod() --> 静态方法:不定义任何参数就可以当函数使用


class B(object):
    @staticmethod   # 等同于第21行
    def foo():
        print "这是静态方法,使用了staticmethod函数,不需要传入self"
    # foo = staticmethod(foo)

b = B()

b.foo()

# classmethod() --> 类方法:传入的参数为类

class C(object):
    bar = 1
    @classmethod
    def foo1(cls):  # 传入的是当前的类,可以调用当前类的属性和方法
        print "这是类方法"
        print cls.bar
    # foo1 = classmethod(foo1)

c  = C()

c.foo1()


