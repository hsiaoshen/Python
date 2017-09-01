#coding=utf-8

# 关于nonlocal的使用(python3中才有)

# 如果在out函数里面定义了inner函数,inner函数如果不在out函数中调用将不会执行而且在全局中调用inner会出错--> 原因是out调用完后会清除内存,此时就没有Inner函数了

def out():
    a = 1    
    print ('out+++++++++')
    def inner():
        print (a)
        # a += 1  # 不能够对定义该函数的作用域中的变量进行修改,只能打印
        nonlocal a  #加nonlocal可以在该代码块内修改该函数所属于的作用域中的变量
        a += 1
        print (a)
        print ('inner--------')
    inner()    
    # global inner  使变量可以在全局中使用,相当于给inner分配了内存空间
out()
# inner()        

