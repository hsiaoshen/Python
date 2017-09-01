#coding=utf-8

# 私有变量和私有方法的访问:使用闭包

class Protect(object):
    def __init__(self):
        self.job = "teacher"
        self.__name = "admin"

    def __python(self):
        print "teach python"

    def getName(self):
        print self.__name

    def setName(self,name = 'admin'):
        if 4<= len(name) <= 8:
            self.__name = name
        else:
            self.__name = self.__name
        

    def getPython(self):
        return self.__python()

class Private(Protect):
    pass

t = Protect()

print t.job
# print t.__name  会出错

t.setName('admina')
t.getName()
t.getPython()

print "+++++++++++++"
t1 = Private()
print t1.job
# print t1.__name 会出错
t1.setName('nihaoma')
t1.getName()
t1.getPython()