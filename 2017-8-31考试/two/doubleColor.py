#coding=utf-8

# 双色球：6蓝色球，数字从1-33随机，1红球，数字从1-16随机，且前6不会重复，使用random模块，打印要求蓝色六个数按升序排列，红球最后

import random

def Blue():
    blueNum = random.randint(1,33)
    return blueNum


def Red():

    redNum = random.randint(1,16)
    return redNum

def show():
    l = []
    count = 0
    while count < 6:
        blue = Blue()
        if blue not in l:   
            l.append(blue)
            count = len(l)
        else:
            continue
    l = sorted(l)
    l.append(Red())   
    print l
    

if __name__ == "__main__":
    show()