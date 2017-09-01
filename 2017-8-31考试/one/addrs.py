# coding=utf-8

def addrs(a,*b):
    try:
        sum = a
        for i in b:
            sum = sum + i
        print sum
    except Exception as e:
        print e
        print '不同类型的不能相加'

if __name__ == '__main__':        
    # addrs('a','1','1')
    # addrs(1,2,34)
    addrs('1',1)



