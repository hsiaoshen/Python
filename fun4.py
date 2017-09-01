#coding=utf-8
a = 1

def f():
    print a
    global b  # 作用是把一个局部变量变成全局可以使用
    b = 3
    print b

f()

print a
print b
