#coding=utf-8

# 不带参数的装饰器和闭包的结合使用

# 其中原先的函数不带参数

# def deco(fun):
#     def _deco():
#         return '这是改造了的函数'
#     return _deco

# @deco
# def fun():
#     return '这是一个原先的函数'

# fun = deco(fun)  <==> @deco

# print (fun())


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 带参数的函数

def deco(fun):
    def _deco(a,b):
        ret =  fun(a, b)
        return a * b + ret
    return _deco

@deco
def fun(a,b):
    return a + b

print(fun(1,2))


# 流程如下: fun(a,b) ==> deco(fun(a,b)) ==> _deco(a,b)    所以fun(1,2) == _deco(1,2) ,由于_deco(a,b)是一个闭包,所以可以使用外部作用域中的变量fun