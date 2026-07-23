"""
案例：nonlocal 关键字介绍

nonlocal:
    它是Python内置的关键字, 可以实现 在内部函数中 修改外部函数的 变量值
"""


# 需求： 编写一个包, 让内部函数访问外部函数的参数 a = 100, 并观察结果

def fn_outer():
    # 定义外部函数的(局部)变量
    a = 100

    def fn_inner(num1):
        nonlocal a
        a = num1 + a
        print(f'a:{a}')
    return fn_inner


if __name__ == '__main__':
    fn_inner = fn_outer()
    fn_inner(1)
    fn_inner(1)
    fn_inner(1)