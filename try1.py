#coding=utf-8


# 和try一起的else,finally,打印具体的错误信息,traceback模块的使用

import traceback

def div(a,b):
    c = None
    try:
        c =  a / b
    except ZeroDivisionError,e:     # 老版本的打印具体信息
        # print 'zero error'
        # print e
        traceback.print_exc()       # 打印出哪里出了什么错误
    
    except TypeError as e:    # 新写法
        # print 'type error'
        # print e
        traceback.print_exc(file = open('tb.txt','w+'))    # 不会打印,会把更详细的错误存储到tb.txt文件中

        a = traceback.format_exc()   # 把详细错误信息赋予一个变量

        print a
    else:
        print 'else +++++++++++'
    
    finally:
        print 'finally -----------'

    return c
# result  =  div(1,'a') # 类型异常
# result = div (1,0)  # 零作被除数异常
result = div(1,1)     # 正常
print result