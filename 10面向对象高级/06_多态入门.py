"""
多态概述：
    同一个函数，可接受不同的参数，有不同的效果
    大白话：同一个事物在不同时刻表现出来的不同状态，形态

    前提条件：
        1. 要有继承
        2. 要有方法重写，不然多态无意义
        3. 要有父类引用指向子类对象
"""


# 定义动物类
class Animal:           # 抽象类（也叫：接口）

    def speak(self):      # 抽象方法
        print("动物会叫")


# 定义子类，狗类
class Dog(Animal):

    def speak(self):
        print("汪汪叫")

# 定义子类，喵类
class Cat(Animal):

    def speak(self):
        print("喵喵叫")


# 定义函数，接收不同的动物对象，调用speak方法
def make_noise(an:Animal):
    an.speak()


if __name__ == '__main__':
    d = Dog()
    c = Cat()

    # 演示多态
    make_noise(d)
    make_noise(c)
