#coding=utf-8

# 继承:定义
# 继承的好处:具有基类的属性,同时还可以进行扩展,这样会减少代码量

class Car(object):
    def __init__(self,name):
        self.name = name
    door = 4

    def run(self):
        print "跑..."  

class Dazhong(Car):
    pass

class Badao(Car):
    seat = 7

class Bense(Car):
    def run(self):
        print "跑的快"

b  = Badao('fengtian')

print b.name
print b.door
print b.seat
b.run()

print '+++++++++'
c = Bense('自由光')

print c.name
print c.door

c.run()