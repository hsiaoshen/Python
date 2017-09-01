#coding=utf-8
import time
from multiprocessing import Process, Pool


def Foo(i):
    
    time.sleep(3)
    # print 100 + i
    return 100 + i

    

def Bar(arg):
    print arg

pool = Pool(5)

# pool.apply,pool.apply_async

for i in range(10):
    pool.apply_async(func = Foo, args=(i,), callback= Bar)  # callback的参数是pool执行完的结果作为参数


    #还是进程的阻塞式执行
    # pool.apply(func = Foo, args=(i,))


# 以下2行必须有,而且顺序不能反
pool.close()
pool.join()