"""
案例：演示通过 self 关键字实现 在类内访问其他函数

self关键字：
    概述：
        代表本类当前对象的引用，谁(哪个对象)调用，self就代表谁
    作用：
        用于实现函数 区分 不同对象的

总结：
    1.在类外 访问类中的行为，需要通过 对象名. 的方式访问
    2.在类中 访问类中的行为 需要通过  self. 的方式访问
"""


# 需求： 定义汽车类， 类内有run()函数，并在work()中调用run()函数，创建该类对象，调用上述的对象.

# 定义汽车类
class Car:
    # 属性（名词）

    # 行为（动词）
    def run(self):
        print(f"{self} 汽车跑起来....")

    def work(self):
        print(f"我是work函数,我的self值：{self}")
        self.run()   # self = 本类当前对象的引用



# 在类外访问Car类的行为（函数）
c1 = Car()
print(f"c1对象：{c1}")
c1.run()   # c1在跑
print("-"*30)
c1.work()   # c1在work,c1在跑
print("-"*30)


# 再次创建对象
c2 = Car()
print(f"c2对象:{c2}")
c2.run()
print("-"*30)
c2.work()
