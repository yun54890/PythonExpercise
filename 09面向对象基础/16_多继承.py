
#
# class Father(object):
#     def run(self):
#         print("run1")
#
# class Mother(object):
#     def run(self):
#         print("run2")
#
#
# class child(Mother,Father):
#     pass
#
#
# if __name__ == '__main__':
#     child = child()
#     child.run()











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

class Prentice(Master,School):
    pass

if __name__ == '__main__':
    prentice = Prentice()
    prentice.make_cake()
    print(Prentice.mro())
    print(Prentice.__mro__)