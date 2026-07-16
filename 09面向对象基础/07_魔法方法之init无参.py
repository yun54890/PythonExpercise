"""
案例：演示 init 魔法方法的 用法

魔法方法：
    概述/特点：
        Python内置的函数，在满足特定的场景下，会被 自动调用
    常见的魔法方法有：
        __init__   在创建对象的时候，会自动触发该类的 __init__() 函数
        __del__
        __str__
"""


# 需求： 定义汽车类，默认属性为： color = "黑色" ,wheel = 3

# 定义汽车类
class Car:
    def __init__(self):
        print("我是魔法方法")
        #  在init魔法方法中，初始化属性，则：该类所有的对象，一创建，就有这些属性了
        self.color = "black"
        self.wheel = 4
    def show(self):
        print(f"颜色值：{self.color} 轮胎数：{self.wheel}")

# 创建汽车类对象
c1 = Car()   # 会自动调用 __init__()函数
c1.color = "red"
c1.wheel = 10
c1.show()
print(c1.color,c1.wheel)
print("-"*30)
#
c2 = Car()
c2.show()