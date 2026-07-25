"""
案例：演示自定义迭代器

迭代器介绍：
    概述：
        自定义的类, 只要重写了 __iter__() 和 __next__() 方法， 就可以称为 迭代器
    目的：
        隐藏底层的逻辑, 让用户使用更方便
        惰性加载, 用的时候才会获取
"""


for i in range(1,10):
    print(i)
print('-'*30)



class Myiterrator:
    def __init__(self,start,end):
        self.current_value=start        # 当前值, 默认为 开始值
        self.end=end                    # 结束值

    # 重写iterator魔法方法,返回当前对象(即：迭代器对象)
    def __iter__(self):
        return self

    # 重写next魔法方法,返回当前值,并更新当前值
    def __next__(self):
        if self.current_value >= self.end:
            raise StopIteration

        value = self.current_value
        self.current_value += 1
        return value



for i in Myiterrator(1,6):
    print(i)


