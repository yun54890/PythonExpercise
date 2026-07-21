"""
该文件用于记录 学生类， 学生的属性信息为：姓名，性别，年龄，手机号，描述信息
"""


class Student:
    # 定义魔法方法，用于初始化属性信息
    def __init__(self,name,gender,age,phone,desc):
        """
        该魔法方法，用于初始化 属性信息.
        :param name: 名字
        :param gender: 性别
        :param age: 年龄
        :param phone: 手机号
        :param desc: 描述
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    def __str__(self):
        return f'名字：{self.name} 性别：{self.gender} 年龄：{self.age} 手机号：{self.phone} 描述：{self.desc}'



if __name__ == '__main__':
    s1 = Student("张三","男",20,'18012341234',"大学本科计算机一班")
    print(s1)