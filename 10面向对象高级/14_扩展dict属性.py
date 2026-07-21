"""
案例：演示Python内置的dict属性

__dict__ 属性介绍：
    它是Python内置的属性,可以把对象转成字典形式
"""
from StudentCMS.student import Student

# 需求1： 把 学生对象 -> 字典形式, 属性名做键,属性值做值
s1 = Student(name='张三', gender='男', age=19, phone='13800138000', desc='喜欢打篮球')
print(s1)

my_dict = s1.__dict__
print(my_dict)
print(type(my_dict))



# 需求2： 把[学生对象, 学生对象, 学生对象] -> [字典, 字典, 字典]
s1 = Student(name='张三', gender='男', age=19, phone='13800138000', desc='喜欢打篮球')
s2 = Student(name='李四', gender='男', age=17, phone='13900139000', desc='爱好编程打代码')
s3 = Student(name='小美', gender='女', age=18, phone='13700137000', desc='喜欢画画追剧')

stu_list = [s1, s2, s3]

# 列表推导式
list_dict = [sku.__dict__ for sku in stu_list]
print(list_dict)

# list_dict = []
# for stu in stu_list:
#     list_dict.append(stu.__dict__)
# print(list_dict)



# 需求3： 把 {'name': '小美', 'gender': '女', 'age': 18, 'phone': '13700137000', 'desc': '喜欢画画追剧'} -> 学生对象
my_dict = {'name': '小美', 'gender': '女', 'age': 18, 'phone': '13700137000', 'desc': '喜欢画画追剧'}
s6 = Student(**my_dict)
print(s6)
print(type(s6))