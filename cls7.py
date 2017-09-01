#coding=utf-8

# super的使用:super(当前类,当前对象).属性 

class Person(object):
    def __init__(self):
        self.height = 160

    def about(self,name):
        print("{} is about {}".format(name,self.height))

class Girl(Person):
    def __init__(self):
        super(Girl,self).__init__()    #可以使用父元素中被覆盖掉的属性和方法
        self.weight = 55
    
    def about(self,name):
        print("{} is a girl,she is about {},and her weight is {}".format(name,self.height,self.weight))
    

Chan = Girl()
Chan.about('DIAOCHAN')

print Chan.weight
print Chan.height

