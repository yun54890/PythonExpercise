"""
案例： 演示单任务, 前边不执行完毕,后边绝对无法执行
"""


def func_a():
    for i in range(10):
        print("hello world")


def func_b():
    for i in range(10):
        print("hello python")


func_a()
print("-"*30)
func_b()