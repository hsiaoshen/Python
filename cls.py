#coding=utf-8

# 类的定义: 
# 格式为  class(关键字) 类名(要继承的,不人为表示继承的类,默认为object):
#                pass

class ClassName(object):
    name = '战狼'  # 成员
    def fun(self):  # 方法,需有个形参self,名字可以随便取,但是约定俗称的叫self,
        print '图图'


print ClassName.name    # 可以直接拿类名来访问类中的私有变量

person = ClassName()   # 实例化要加括号,不加括号叫做赋值

person.age = 18    # 给实例化对象特有的属性,其他的实例化对象没有

print '--------',person.name,person.age

person.fun()

a = ClassName  # 这是把类赋给了a

a.age = 19   # 可以给类赋值法添加新的成员

print a.name,a.age

a.name = "小狼"  #可以修改类的成员

b = a()  # a也是一个类,可以实例化

print '+++++',b.name,b.age




