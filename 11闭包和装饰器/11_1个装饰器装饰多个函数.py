"""
案例：演示 带参数的装饰器

记忆：
    1. 1个装饰器的参数有且只能有 1个
    2. 如果装饰器有多个参数, 可以在该装饰器的外边再包裹一层, 把该装饰器当作其 内部函数 返回即可
"""



# 需求: 定义1个既能装饰减法,又能装饰加法的装饰器 -> 即： 带有参数的装饰器

def loggin(flag):
    def my_decorator(fn_name):     # fn_name: 原有函数名. flag:标记
        def fn_inner(a,b):
            if flag == '+':
                print("正在努力[加法]计算...")
            elif flag == '-':
                print("正在努力[减法]计算...")
            return fn_name(a,b)
        return fn_inner
    return my_decorator

@loggin('+')
def get_sum(a,b):
    return a+b

@loggin('-')
def get_sub(a,b):
    return a-b




if __name__ == '__main__':
    sum =  get_sum(1,2)
    print(sum)

    sum = get_sub(1,2)
    print(sum)