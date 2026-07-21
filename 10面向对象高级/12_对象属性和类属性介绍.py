"""
案例：演示对象属性 和 类属性

属性介绍：
    概述：
        它是1个名词，用来描述事物的外在特征的
    分类：
        对象属性： 属于每个对象的，即： 每个对象的属性值可能都不同， 修改A对象的属性，不影响对象B
        类属性： 属于类的，即：能被该类下所有的对象所共享，A对象修改类属性，B对象访问的是修改后的

对象属性：
    定义到 init 魔法方法中的属性，每个对象都有自己的内容
    只能通过 对象名. 的方式调用

类属性：
    定义到类中，函数外的属性(变量)，能被该类下所有的对象所共享
    既能通过 类名. 还能通过 对象名. 的方式来调用，推荐使用类名. 的方式
"""


class Stuent:
    # 定义类属性
    teacher_name = "水镜先生"

    # 定义对象属性，即： 写到 init 魔法方法中的属性
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名：%s,年龄: %d'%(self.name,self.age)



if __name__ == '__main__':
    s1 = Stuent("曹操",20)
    s2 = Stuent("曹操",20)

    s1.name="张三"
    s1.age=90

    print(s1)
    print(s2)

    print(s1.teacher_name)
    print(s2.teacher_name)
    print(Stuent.teacher_name)
    print("-"*20)

    s1.teacher_name = "123"
    print(s1.teacher_name)
    print(s2.teacher_name)
    print(Stuent.teacher_name)
    print("-" * 20)

    Stuent.teacher_name = "321"
    print(s1.teacher_name)
    print(s2.teacher_name)
    print(Stuent.teacher_name)
    print("-" * 20)