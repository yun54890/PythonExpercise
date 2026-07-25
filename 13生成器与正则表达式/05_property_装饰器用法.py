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

    之后, 就可以直接 上述的函数名 来当做变量直接使用
"""



class student:
    def __init__(self):
        self.__age = 180

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age = age


if __name__ == '__main__':
    s = student()
    s.age= 20
    print(s.age)
