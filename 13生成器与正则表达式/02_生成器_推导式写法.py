"""
案例：演示生成器之 推导式写法.

生成器介绍：
    概述：
        所谓的生成器就是基于 数据规则, 用一部分在生成一部分, 而不是一下子生成完所有.
    目的：
        可以节省大量的内存
    实现方式：
        1. 推导式
        2. yield关键字
"""
import sys

# 列表推导式：方括号 []
list = [i for i in range(1,11)]
print(list)
# [] -> 列表推导式
# () -> 生成器表达式, 创建生成器对象




# 生成器表达式：圆括号()
my_generator = (i for i in range(1,11))
print(my_generator)
print(type(my_generator))        # <class 'generator'>
print("-"*30)


my_gt2 = (i for i in range(1,11) if i % 2 == 0)
print(my_gt2)
print("-"*30)



print(next(my_gt2))
print(next(my_gt2))
print("-"*30)
for i in my_gt2:
    print(i)
print("-"*30)


# 验证 生成器的目的 就是可以减少内存占用.
my_list = [i for i in range(10000000)]
my_gt3 = (i for i in range(10000000))
print(type(my_list),type(my_gt3))

print(f"my_list的内存占用：: {sys.getsizeof(my_list)}")
print(f"my_gt3的内存占用：: {sys.getsizeof(my_gt3)}")


