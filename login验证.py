#coding=utf-8

# 实现注册的内部校验,若小于4或者大于8给其一个默认的名字

def reg_check(arg):
    def reg(reg):
        def regc(name):
            ret = reg(name)
            if 4<= len(ret) <= 8:
                return ret
            else:
                return arg
        return regc
    return reg

@ reg_check('admin')
def reg(name):
    return name

name = raw_input()

print reg(name)