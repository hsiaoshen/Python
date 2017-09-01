#coding=utf-8

# 闭包:在函数调用结束后,还能记住当前环境以及自由变量
# 好处是:减少全局环境空间被污染

def maker(N):
    def action(X):
        return X ** N
    return action

f = maker(2)   # 此时maker的内存空间被清除

print(f(3))   # 但是还能使用N变量