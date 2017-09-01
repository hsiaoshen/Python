#coding=utf-8

# t.send()的使用会向迭代对象中传值,若有原值会被覆盖,但是必须先让迭代器运行取来

import time

def fib(max):
    a,b = 0,1
    while a < max:
        k = yield 
        a,b = b, a + b
        print '+++++++++',k

t = fib(20)

# t.next()
t.send(None)

while True:
    time.sleep(1)
    t.send(10)   