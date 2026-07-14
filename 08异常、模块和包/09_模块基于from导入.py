"""
from 模块名  import  功能  [as 别名]

用的时候:
功能名
就可以直接用了
不需要  模块.功能


假设模块叫做A,内部有3个功能分别是A1,A2,A3
如果 import A 导入
则用这个功能需要: A.A1  A.A2  A.A3

如果是from写法则,可以
from A import A1
直接用A1
"""

# 需求还是用random模块的randint生成随机数
# import random as r

# r.randint()

# 可以直接用randint函数名
# from random import randint
# randint(1,10)


# 可以直接用别名代替原有的名称
from random import randint as r
r(1,10)