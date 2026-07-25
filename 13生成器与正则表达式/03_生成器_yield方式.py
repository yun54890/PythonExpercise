"""
案例：演示生成器之 yield写法.

生成器介绍：
    概述：
        所谓的生成器就是基于 数据规则, 用一部分在生成一部分, 而不是一下子生成完所有.
    目的：
        可以节省大量的内存
    实现方式：
        1. 推导式
        2. yield关键字
"""


def my_fun():
    # my_list = []
    # for i in range(1,10):
    #     my_list.append(i)
    # return my_list

    # 效果类似上述的代码
    # yield在这里做了三件事情：1. 创建生成器对象  2. 把值存储到生成器中  3. 返回生成器
    for i in range(1,11):
        yield i



if __name__ == '__main__':
    my_gt1 = my_fun()
    print(type(my_gt1))         #<class 'generator'>

    print(next(my_gt1))
    print(next(my_gt1))
    print("-"*30)
    for i in my_gt1:
        print(i)
