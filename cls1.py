#coding=utf-8

# self的详解:指向实例化对象本身,而不是类本身,原因是如果指向类且有多个实例化对象,self就不知道指向哪一个对象了(类似于js中的this)
# 不需要给self单独传参,自动绑定实例化对象

class Person(object):
    age = 12
    def __init__(self,name):   # __init__(self)  对象的初始化函数,实例化对象自动执行,不需要调用
        print self
        # self.age = self.age + 1
        self.name = name
    def change_age(self,num):
        self.age = self.age + num

a = Person('小明')    # 类中的参数给特定的方法传参
b = Person('小李')

a.change_age(1)
b.change_age(-1)

print a.age
print a.name

print b.age
print b.name