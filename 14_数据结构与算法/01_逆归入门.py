"""
案例：演示逆归入门

逆归介绍：
    概述：
        方法自己调用自己的情况就叫逆归
    经典案例：
        1. 求阶乘
        2. 不死神龟
        3. 文件夹拷贝,删除等...
        4. 服务器文件整理
"""


# const = 0
# def show():
#     global const
#     const +=1
#
#     print(const)
#
#     if const >= 100:
#         return
#     show()

sum = 1
def factorial(n):
    # global sum
    # sum *= n
    # n -=1
    # if n == 0:
    #     return
    # factorial(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)



if __name__ == '__main__':
    print(factorial(5))