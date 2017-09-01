#coding=utf-8

# 从终端输入一个字符串,将字符串中的空格替换称'-',然后返回替换后的字符串

def f(char):
   l = char.split(' ')
   print l
   k = '-'.join(l)
   return k  
l = f('hello world')

print l      