

def say_hi():
    print("hello world")

def wangwang():
    print("B汪汪")

def add(x,y):
    print(x+y)

name = "周杰伦"
age = 11
height = 172.23


# 如果本文件被直接执行,则内置变量 __name__ 会被赋值为: "__main__"
# 如果本文件被import或from导入,则内置变量__name__会被赋值为: 文件名称
# __name__是python内置变量,任何代码文件都有
# 我们可以通过读取这个变量的值,从而确定这个代码文件是:被人导入了 还是被作为程序执行了
if __name__ == '__main__':
    say_hi()