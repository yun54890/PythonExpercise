"""
案例： 演示魔法方法之 init 有参 ,实际开发常用

回顾：
    __init__()魔法方法，在创建对象的时候，会被自动调用，一般用于给该类对象，

大白话举例：
    无参init -> 默认上的有底色，你需要重新涂色（覆盖底色）
    有参init -> 默认没有涂色的石膏娃娃，我们根据喜好自由涂色即可
"""


# 需求：创建汽车类，不给默认值，由汽车对象 外部各自赋值即可
# 1. 定义汽车类
class Car:
    # 2. 有参的 __init__函数，参数值由：外部对象自行赋值
    def __init__(self,color,wheel):
        """
        该魔法方法用于给 汽车类 对象的属性 赋值.
        :param color: 车的颜色
        :param wheel: 车的轮胎数
        """
        self.color = color
        self.wheel = wheel

    # 定义show()函数，打印该类对象的 各个属性值
    def show(self):
        print(f"颜色值：{self.color},轮胎数：{self.wheel}")


# 3. 创建汽车类对象
c1 = Car("红色",5)   # 默认调用了init()函数，但是该函数有参数，则必须传参.
c1.show()
print("-"*30)

c2 = Car("粉色",10)
c2.show()