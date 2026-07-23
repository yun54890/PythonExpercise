"""
案例： 无参有返回的原函数

细节：
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致
    即： 原函数是无参无返回的, 则 装饰器的内部函数也必须是 无参无返回的
        原函数有参有返回的，则 装饰器的内部函数也必须是 有参有返回的
"""


def decorator_outer(fn_name):
    def decorator_inner():
        print("正在努力计算中...")
        return fn_name()
    return decorator_inner

# @decorator_outer
def get_sum():
    a = 10
    b = 20
    return a + b



if __name__ == '__main__':
    # sum = get_sum()
    # print(f"{sum}")

    get_sum = decorator_outer(get_sum)
    sum = get_sum()
    print(sum)