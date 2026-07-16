"""
案例：演示 init 魔法方法的 用法

魔法方法：
    概述/特点：
        Python内置的函数，在满足特定的场景下，会被 自动调用
    常见的魔法方法有：
        __init__   在创建对象的时候，会自动触发该类的 __init__() 函数
        __str__    当用print()函数 打印对象的时候，会自动调用该对象(所在类)的 str魔法方法.
                   该魔法方法默认打印的是对象的地址值，无意义，一般都会重写，该为打印 对象的各个属性值
        __del__    当.py执行结束之后，或者 手动del 释放对象资源，会自动调用该函数
"""


#  1. 定义汽车类，属性：品牌.       行为：run()   通过del魔法方法删除该类的对象，看看效果
class Car:
    # 2. 在魔法方法init中,完成：属性的初始化
    def _init__(self,brand):
        self.brand = brand
    # 3. 重写 str魔法方法，打印对象的属性值.
    def __str__(self):
        return f"品牌：{self.brand}"

    # 4. 重写 del魔法方法，删除对象时给出提示.
    def __del__(self):
        print(f"{self}对象被删除了")


#  创建对象及定义属性
c1 = Car()
c1.brand = "宝马"
print(c1)

# 访问 brand 属性
print(c1.brand)
print("-"*20)

# 删除c1对象
del c1
# print(c1)

print("程序结束")