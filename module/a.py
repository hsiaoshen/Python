#coding=utf-8

# 模块导入
# 包的导入: 必须在包下面有个__init__.py文件

import b as B
# reload(b)    # 若要多次导入同一个模块

print B.c

B.b()


a = B.A()

# 用import导入一个包，但是路径过长不建议使用
import dir.d

dir.d.d()

# 路径过长
from dir.dir1.e import e

e()

# 调用__init__.py文件中的属性和方法
from dir.dir1 import *

initFun()

print ctime()