"""

继承介绍：
    概述：
        大白话；子承父业
        专业版：子类可以继承父类的属性 和 行为
    写法：
        class 子类名(父类名):
            pass
    例如：
        class A(B):
            pass
    叫法：
        A: 子类，派生类
        B: 父类，基类，超类
    好处：
        提高代码的复用性
    弊端：
        耦合性增强了，父类不好的内容，字类想没有都不行
    扩展 ： 开发原则
        高内聚，低耦合
        内聚：指的是类自己独立处理问题的能力
        耦合：指的是类与类之间的关系
        大白话解释：自己能搞定的事儿，就不要麻烦别人
"""


# 定义父类
class Father(object):
    def __init__(self):
        self.gender = 'male'

    def walk(self):
        print("饭后走一走，活到九十九！")

# 定义子类
class son(Father):
    pass


if __name__ == '__main__':
    s = son()
    print(f"性别:{s.gender}")
    s.walk()