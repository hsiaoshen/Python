#coding=utf-8

from  c import * 

 # 可以把另一个命名空间的属性导入到当前命名空间,可以直接用
from  c import _C

# 但是对于受保护的属性或者类,必须具体引入,而不能使用 *

class A(object):
    pass

def b():
    print '函数'

c = 1

print '这是顶层代码'

fc()    # 直接用,不需要c.fc()

d = _C()    # 受保护的类生成对象

print d.name
