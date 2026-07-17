"""

思路：
    1. 父类名.父类函数名(self)        精准访问，想找哪个父类，就调用哪个父类
    2. super().父类函数名()          只能访问最近的那个父类，有就用，没有就报错

"""



class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu} 制作煎饼果子")
    # pass


class School(object):
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu} 制作煎饼果子")
        # pass


class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '[自己的独家煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu} 制作煎饼果子")

    def make_old_cake(self):
        super().__init__()
        super().make_cake()

if __name__ == '__main__':
    prentice = Prentice()
    print(prentice.kongfu)
    prentice.make_cake()
    print("-"*30)

    prentice.make_old_cake()