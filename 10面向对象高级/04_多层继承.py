"""

多层继承解释：
    类A继承类B,类B继承类C，这就是多层继承

"""



# 当前的继承体系
#  object <- Master, School <- Prentice <- Tusun

class Master:
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu} 制作煎饼果子")



class School:
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu} 制作煎饼果子")



class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '[自己的独家煎饼果子配方]'

    def make_cake(self):
        print(f"运用{self.kongfu} 制作煎饼果子")


    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class TuSun(Prentice):
    pass


if __name__ == '__main__':
    ts = TuSun()
    ts.make_cake()
    ts.make_school_cake()
    ts.make_master_cake()