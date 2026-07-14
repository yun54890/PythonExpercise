"""
import A
A.A1()
A.A2()
...

from A import A1,A2
A1()
A2()
"""

# import B
# B.say_hi()
# B.wangwang()
# print(B.name)
# print(B.age)
# print(B.height)
#
# print("-"*20)
# from B import say_hi,wangwang,add
# say_hi()
# wangwang()


# 如果导入同名的功能,则后导入的生效
# from B import wangwang
# from C import wangwang
# wangwang()

from C import *
hi()
info()
miaomiao()