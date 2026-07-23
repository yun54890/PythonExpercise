"""

"""


# 位置参数求和
# 编写一个函数 sum_all(*args)，接受任意数量的数字，返回它们的总和。
def sum_all(*args):
    # MethodOne
    sum = 0
    for i in args:
        sum += i
    return sum

    # MethodTwo
    # return sum(args)



# 关键字参数值求和
# 编写一个函数 sum_kwargs(**kwargs)，接受任意数量的关键字参数（值都是数字），返回所有值的总和。
def sum_kwargs(**kwargs):
    # MethodOne
    sum = 0
    for v in kwargs.values():
        sum += v
    return sum

    # MethodTwo
    #return sum(kwargs)


# 混合使用 *args 和 **kwargs
# 编写一个函数 combine_sum(*args, **kwargs)，返回所有位置参数和关键字参数值的总和。
def combine_sum(*args,**kwargs):
    sum = 0
    for i in args:
        sum += i
    for v in kwargs.values():
        sum += v
    return sum


# 强制必填参数 + 可变参数
# 编写一个函数 multiply_and_add(base, *args, **kwargs)，它接受一个必填位置参数 base，然后：
#   将所有位置参数（args）相乘，得到一个乘积；
#   将所有关键字参数的值（kwargs.values()）相加，得到一个和；
#   返回 base * 乘积 + 和。
def multiply_and_add(base,*args,**kwargs):
    sum_val = 0
    product = 1
    for i in args:
        product *= i
    for v in kwargs.values():
        sum_val += v
    return base * product + sum_val


# 解包实战
# 已知有一个函数 def greet(name, age, city): print(f"{name} is {age} years old from {city}")。
# 现在你有一个列表 info_list = ["Alice", 25] 和一个字典 info_dict = {"city": "New York"}。
# 请使用 列表解包（*） 和 字典解包（**） 来调用 greet 函数，使得输出为：
# Alice is 25 years old from New York

def greet(name,age,city):
    print(f"{name} is {age} years old from {city}")


# 编写一个装饰器
# 编写一个装饰器 log_call，它装饰任何函数，并在函数执行前打印出传入的所有参数（包括位置参数和关键字参数）。
# 要求：装饰器内部使用 *args 和 **kwargs 来接收原函数的所有参数，并原样传递。

def log_call(fn_name):
    def fn_inner(*args,**kwargs):
        fn_name(*args,**kwargs)
        return(f"位置参数{args},关键字参数{kwargs}")
    return fn_inner

@log_call
def add(a,b):
    return a+b


if __name__ == '__main__':
    # 基础 - 位置参数求和
    print(sum_all(1, 2, 3))
    print(sum_all(10, 20, 30,40))
    print(sum_all())
    print("-"*30)

    # 关键字参数值求和
    print(sum_kwargs(a=1, b=2, c=3))
    print(sum_kwargs(x=10,y=20))
    print(sum_kwargs())
    print("-"*30)

    # 混合使用 *args 和 **kwargs
    print(combine_sum(1, 2, a=3, b=4))  # 输出 1+2+3+4 = 10
    print(combine_sum(5, 6))  # 输出 11（仅有位置参数）
    print(combine_sum(x=7, y=8))  # 输出 15（仅有关键字参数）
    print("-" * 30)

    # 强制必填参数 + 可变参数
    print(multiply_and_add(2, 3, 4, a=1, b=2))
    # 解释: base=2, args=(3,4) -> 乘积=3*4=12, kwargs={a:1,b:2} -> 和=3, 结果=2*12+3=27
    print(multiply_and_add(5, 1, 2, 3))  # args乘积=6, 没有kwargs和=0, 结果=5*6+0=30
    print(multiply_and_add(10, x=1, y=2))  # args为空乘积=1（空乘积应返回1）, 和=3, 结果=10*1+3=13
    print("-" * 30)


    # 解包实战
    info_list = ["Alice", 25]
    info_dict = {"city": "New York"}
    greet(*info_list,**info_dict)
    print("-" * 30)

    # 编写一个装饰器
    print(f"调用add, {add(3, 5)}")
    print(f"调用add, {add(4, b=6)}")
