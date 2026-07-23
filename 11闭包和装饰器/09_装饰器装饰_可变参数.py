"""
案例： 有参有返回的原函数

细节：
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致
    即： 原函数是无参无返回的, 则 装饰器的内部函数也必须是 无参无返回的
        原函数有参有返回的，则 装饰器的内部函数也必须是 有参有返回的
"""



def decorator_outer(fn_name):
    def decorator_inner(*args, **kwargs):
        print("正在计算中...")
        return fn_name(*args, **kwargs)
    return decorator_inner


@decorator_outer
def get_sum(*args,**kwargs):
    """
    该函数用于计算 数字列表 和 字典value值 之和
    :param args: 数字列表  *args -> 接收所有的位置参数, 封装到 元组
    :param kwargs: 字典, 键是字符串,值是数字, **kwargs -> 接收所有的关键字参数, 封装到 字典
    :return: 结果之和
    """
    # 定义求和变量
    # sum = 0
    # # 遍历元组, 获取每个元素, 求和
    # for i in args:
    #     sum += i
    # # 遍历字典, 获取到每一个值.
    # for v in kwargs.values():
    #     sum += v
    # return sum

    return sum(args) + sum(kwargs.values())

if __name__ == '__main__':
    sum = get_sum(1,2,3,4,1,2,3,4)
    print(sum)