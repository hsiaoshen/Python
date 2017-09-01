#coding=utf-8

# 一般不用写东西

from time  import ctime

def initFun():
    print '这是定义在__init__.py中的函数，可以通过__all__被导入当前包的模块中使用'

__all__ = ['ctime','initFun'] 