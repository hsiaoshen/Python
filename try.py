#coding=utf-8

# 异常的捕获和处理,try来捕获异常,except来处理异常

def div(a,b):
    try:
        return a / b

    #1 如果except后面什么都不写,那么只要遇到异常都用同一种解决方案,但是不建议写
    # except:
    #     print "这是个异常"

    #2
    # except Exception:
    #     print '这是允许的新写法,Exception是异常的基类'

    #3  一个try可以有多个except,遇到哪个异常找对应的处理

    # except ZeroDivisionError:
    #     print 'zero为除数错误'
    
    # except TypeError:
    #     print '类型错误'

    #4 except后面可以跟多个异常(一个元组),但是不会差异化处理异常

    except (ZeroDivisionError,TypeError):
        print '共用一个错误'

    #5 如果遇到的异常没有对应的处理,那么还是会报异常错误

result = div(1,'a')
print result