#coding=utf-8

# global的作用:使全局变量可以在函数代码块中进行修改,若不加global,那么只能打印

a = 5

def f():
    print a
    global a  
    a +=1  
    print a

print a
print '++++++++++++++++'
f()

