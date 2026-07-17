"""

重写解释：
    概述：
        重写也叫覆盖，即：子类出现和父类重名的属性 或者 行为， 称之为：重写
    调用层次：
        遵循 就近原则，子类有就用，没有就去就近的父类找，依次查找其所有的父类，有就用，没有就报错
"""







class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu} 制作煎饼果子")


class School(object):
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu} 制作煎饼果子")


class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '[自己的独家煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu} 制作煎饼果子")

if __name__ == '__main__':
    prentice = Prentice()
    prentice.make_cake()
    