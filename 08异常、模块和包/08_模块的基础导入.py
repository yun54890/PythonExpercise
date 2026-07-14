

"""
import 模块名
模块名:文件名
import time
本质就是导入一个叫做time.py的文件, 这个time.py 是python官方自带的


导入后就可以用
模块名.函数
模块名.变量
模块名.类(暂时没学)

"""

import time as t
import random

random.randint(1,10)
t.time()

print("hello")
t.sleep(5)
print("world")