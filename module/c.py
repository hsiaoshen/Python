#coding=utf-8
def fc():
    print 'this is c module'

class _C(object):
    name = 'lisi'

print __name__   # 当前为顶层模块:'__main__'    被其他调用: 模块名

if __name__ == '__main__':
    print 'success'