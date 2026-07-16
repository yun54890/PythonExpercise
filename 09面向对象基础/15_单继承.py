"""
案例： 单继承，即：1个子类继承自1个父类
"""


class Master(object):
    def __init__(self):
        self.kongfu = '[古法配方]'

    def make_cake(self):
        print(f"采用{self.kongfu}摊煎饼果子")


class Prentice(Master):
    pass

if __name__ == '__main__':
    prentice = Master()
    prentice.make_cake()
    prentice.make_cake()