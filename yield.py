#coding=utf-8

# 生成器


# yield的作用是阻塞,若没有迭代器就会阻塞代码的执行,yield就相当于返回一个值,每次只读取一次,但是不会影响函数的结束

def fun():
    print 'The yield test'
    yield 5
    print '被阻塞了吗'

k = fun()

print k

for i in k:
    print k.next()

# print k.next()