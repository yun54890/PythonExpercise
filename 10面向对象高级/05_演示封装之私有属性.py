"""
封装简介：
    概述：
        属于面向对象的三大特征之一，就是隐藏对象的属性和实现细节，仅对外提供公共的访问方式
    怎样封装？
        我们学的 函数，类，都是封装的体现
    好处：
        1. 提高代码的安全性          # 私有化 来保证
        2. 提高代码的复用性          # 函数 来保证
    弊端：
        代码量增加了，因为私有内容外界想访问，必须提供公共的访问方式，代码量就增加了

"""


class Prentice:
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'
        self.__money = 10999898

    def make_cake(self):
        print(f"运用{self.kongfu}制作煎饼果子")

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

class TuSun(Prentice):
    pass

if __name__ == '__main__':
    ts = TuSun()
    ts.make_cake()

    ts.set_money(100)

    # print(ts.__money)   # 报错， 父类私有成员，子类无法访问
    print(ts.get_money())    #   通过父类提供的公共访问方式，访问父类的私有成员