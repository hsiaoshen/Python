# coding=utf-8

# raise的作用:(1)手动抛出人为设定的异常 (2) 终止程序执行

class MyError(Exception):
    pass

try:
    s = None
    if s is None:
        print ('s 是空对象')               # 执行的第一步
        raise MyError('This is error')     # 执行第二步
    print (len(s))                          # 终止
except MyError as e:
    print ('空对象没有长度')                 # 第三步 
    print (e.args)                         # 第四步

# 以下为输出结果

# s 是空对象
# 空对象没有长度
# ('This is error',)