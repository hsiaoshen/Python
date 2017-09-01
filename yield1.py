#coding=utf-8

def fib(max):
    a,b = 0,1
    while a < max:
        yield a
        a,b = b, a + b
        print '+++++++++'

t = fib(20)

# print t.next()   # 结果为0,而且一直为0,原因是只读取一次

while True:
    print  t.next()    # 感觉像抛出去才执行后面的