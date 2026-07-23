"""
案例： 无参无返回的原函数

细节：
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致
    即： 原函数是无参无返回的, 则 装饰器的内部函数也必须是 无参无返回的
        原函数有参有返回的，则 装饰器的内部函数也必须是 有参有返回的
"""


def fn_outer(fn_name):
    def fn_inner():
        print("正在努力计算中..")
        fn_name()
    return fn_inner

@fn_outer
def get_sum():
    a = 10
    b = 20
    sum = a + b
    print(f"sum ={sum}" )



if __name__ == "__main__":
    # 传统方式
    # fn_inner = fn_outer(get_sum)
    # fn_inner()


    get_sum()