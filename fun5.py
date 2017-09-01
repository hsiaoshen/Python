#coding=utf-8

# 内建函数:globals() locals()

a = 1
b = 2

def fun():
    c = 3
    d = 4
    print locals()   # 打印出局部作用域下的环境变量组成的字典

print globals()  #打印出全局环境下的全局量组成一个字典

# {'a': 1, 'b': 2, '__builtins__': <module '__builtin__' (built-in)>, '__file__': 'fun5.py', '__package__': None, 'fun': <function fun at 0x7fc4a88c7758>, '__name__': '__main__', '__doc__': None}

fun()

# {'c': 3, 'd': 4}