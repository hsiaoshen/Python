#coding=utf-8

# 多重继承:中间用逗号隔开
# 遇到相同属性名时,按深度优先遍历使用最优的值
# 对于简单的多重继承,可以认为哪个类在前面,可以优先使用该类同名的属性

class Calculator(object):
    name ="luosifu"

    age = 88
class Talker(object):
    name = "liyong"

    sex ='man'

class TalkCalculator(Calculator,Talker):
    pass

A = TalkCalculator()

print A.name
print A.sex
print A.age

print TalkCalculator.__mro__   # 打印遍历的顺序
