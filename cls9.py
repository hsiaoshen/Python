#coding=utf-8

# 魔法方法:以下划线开始,下划线结束

# 三引号的作用(1)可以做多行注释(2)保留字符串的格式(3)作为文档内容

''' THis is a doc '''    # 这就是注释,在交互模式中用cls9.__doc__可以显示

class A(object):
    '''This is a class A document'''   # 这是类中的内容

# 注意:__new__(cls)和__init__(self)的参数不同,而且__new__(cls)先执行
    def __init__(self):
        print '这是一个对象创建就执行的函数'

    def __new__(cls):
        print "这是一个__new__函数,对象生成器"
        return super(A,cls).__new__(cls)  # 使用super()函数可以生成对象,可以控制对象生成,若没这一步,就生不成对象,可写单例模式

    def __del__(self):
        print '销毁时才执行'

    def __call__(self,a):
        print '这可以把对象当函数使用,也可以传参',a

    def __getattr__(self,name):
        print 'You use getattr on attr %s'%name
        return

    def __setattr__(self,name,value):
        print "You use setattr"
        self.__dict__[name] = value
        

    def __delattr__(self,name):
            print "You use delattr"

    def __getitem__(self,key):
        return self.dict[key]

    def __setitem__(self,key,value):
        self.dict[key] = value

    def __len__(self):
        return len(self.dict)


a = A()

print "=================="
a['a'] = 1
print a['a']
print len(a)
print "===================="
a(1)  # 调用了call
#del a
print a.__doc__
print a.__module__

a.value = 100
print a.value

del a.value