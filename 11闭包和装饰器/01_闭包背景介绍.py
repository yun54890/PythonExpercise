"""
案例：闭包背景介绍

案例目的：
    引出来 闭包 相关的知识点
"""

# 需求：定义函数保存变量10，调用函数返回值 并 重复累加数值，观察结果

def func():
    num = 10
    return num

num = func()
print(num + 1)
print(num + 1)
print(num + 1)