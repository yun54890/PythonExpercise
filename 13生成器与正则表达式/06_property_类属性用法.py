"""
案例：演示property属性的用法

property属性介绍：
    概述/目的/作用:
        把 函数 当成变量来使用
    实现方式：
        方式1：装饰器
        方式2：类属性



property的装饰器用法：
    @property                    # 修饰 获取值的函数
    @获取值的函数名.setter          #  设置值的函数

property类属性的用法：
    类属性名 = property(获取值的函数名,设置值的函数名)

    之后, 就可以直接 上述的函数名 来当做变量直接使用
"""


class Student:
    def __init__(self):
        self.__age = 20

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age



    # 参1：获取值的函数名  参2: 设置值的函数名
    age = property(get_age,set_age)

if __name__ == '__main__':
    s = Student()
    s.age = 99
    print(s.age)