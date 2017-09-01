#coding=utf-8

# 带参数的装饰器,需在外层添加函数

def deco(arg):
    def _deco(fun):
        def __deco(a,b):
            print "before"
            ret = fun(a,b)
            print ret
            print "after"
            return ret * arg
        return __deco
    return _deco

@deco(2)

def fun(a,b):
    return a + b
print fun(1,2)