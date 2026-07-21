"""
该文件用于 完成学生管理系统的 具体业务的操作，即：增删改查，保存学生信息...
"""

# 导包
from student import Student
import time

# 创建学生管理系统类
class StudentCMS(object):
    # 通过魔法方法init, 初始化属性信息
    def __init__(self):
        # 创建一个空列表, 用于存储学生信息.
        self.stu_list = []    # [学生对象，学生对象，学生对象] -> [Student(...),Student(...)...]
        # self.stu_list = [
        #     Student(name='张三', gender='男', age=19, phone='13800138000', desc='喜欢打篮球'),
        #     Student(name='李四', gender='男', age=17, phone='13900139000', desc='爱好编程打代码'),
        #     Student(name='小美', gender='女', age=18, phone='13700137000', desc='喜欢画画追剧'),
        #     Student(name='小雨', gender='女', age=20, phone='13600136000', desc='平时爱看书'),
        #     Student(name='阿凯', gender='男', age=18, phone='13500135000', desc='擅长游泳'),
        #     Student(name='婷婷', gender='女', age=19, phone='13400134000', desc='喜欢弹吉他'),
        #     Student(name='浩然', gender='男', age=20, phone='13300133000', desc='喜欢骑行'),
        #     Student(name='思琪', gender='女', age=17, phone='13200132000', desc='爱吃甜品烘焙'),
        #     Student(name='俊熙', gender='男', age=18, phone='13100131000', desc='热爱摄影'),
        #     Student(name='若曦', gender='女', age=19, phone='13000130000', desc='喜欢旅游探店'),
        # ]

    # 定义函数，实现打印 管理系统的界面
    @staticmethod
    def show_view():
        print('*'*35)
        print("本学员管理系统v2.0可完成如下操作：")
        print("\t1.添加学员;")
        print("\t2.修改学员;")
        print("\t3.删除学员;")
        print("\t4.查询某个学员;")
        print("\t5.显示所有学员;")
        print("\t6.保存信息;")
        print("\t0.退出系统.")
        print('*'*35)
        print()


    #  定义函数, 实现添加学生信息功能
    def add_student(self):
        name = input('请输入学生姓名：')
        gender = input('请输入学生性别：')
        age = int(input('请输入学生年龄：'))
        phone = input('请输入学生手机号：')
        desc = input('请输入学生描述信息：')
        stu = Student(name, gender, age, phone, desc)
        self.stu_list.append(stu)
        print(f'添加 {name} 学生信息成功\n')

    #  定义函数, 实现删除学生信息功能
    def del_student(self):
        del_name = input("请输入要删除的学生姓名：")
        for stu in self.stu_list:
            if stu.name == del_name:
                self.stu_list.remove(stu)
                print(f'学员 {del_name} 信息删除成功')
                print()
                break
        else:
            print("查无此人，请检查后重新删除")

    #  定义函数, 实现修改学生信息功能
    def update_student(self):
        update_name = input("请输入要修改的学生姓名：")
        for stu in self.stu_list:
            if stu.name == update_name:
                stu.age = int(input('请录入修改后的年龄：'))
                stu.gender = input('请录入修改后的性别：')
                stu.phone = input('请录入修改后的电话：')
                stu.desc = input('请录入修改的描述信息：')
                print(f'学员 {update_name} 信息修改成功')
                break
        else:
            print("查无此人，请检查后重新删除")

    #  定义函数, 实现查询单个学生信息功能
    def search_one_student(self):
        search_name = input("请输入要查询的学生姓名：")
        for stu in self.stu_list:
            if stu.name == search_name:
                print(stu,end='\n\n')
                break
        else:
            print("查无此人，请检查后重新查找")

    #  定义函数, 实现查询所有学生信息功能
    def search_all_student(self):
        if len(self.stu_list) == 0:
            print("暂无学生信息")
        else:
            for stu in self.stu_list:
                print(stu)
            print()

    #  定义函数, 实现保存学生信息功能
    def save_student(self):
        # 关联 学生信息文件
        with open('./stu_data.txt','w',encoding='utf-8') as dest_f:
            stu_dict = [stu.__dict__ for stu in self.stu_list]
            dest_f.write(str(stu_dict))
            print('保存学生信息成功！')

    # 定义函数, 实现加载学生信息.
    def load_student(self):
        try:
            with open('./stu_data.txt','r',encoding='utf-8') as src_f:
                stu_data = src_f.read()
                stu_list = eval(stu_data)
                if len(stu_list) == 0:
                    stu_list = []
                self.stu_list = [Student(**stu_dict) for stu_dict in stu_list]
        except:
            with open('./stu_data.txt','w',encoding='utf-8') as src_f:
                pass

    # 定义函数, 把上述的所有业务逻辑跑通
    def start(self):
        self.load_student()
        while True:
            time.sleep(1)
            # 调用函数，打印学生管理系统的界面
            StudentCMS.show_view()

            # 提示用户录入要操作的编号，并接收
            input_num = input('请输入您要操作的编号：')

            if input_num == '1':
                self.add_student()

            elif input_num == '2':
                self.update_student()

            elif input_num == '3':
                self.del_student()

            elif input_num == '4':
                self.search_one_student()

            elif input_num == '5':
                self.search_all_student()

            elif input_num == '6':
                self.save_student()

            elif input_num == '0':
                # 退出系统，做二次校验
                num = input('您确定要退出吗？(Y/N) ->')
                if num.lower() == 'y':           # 字母串的lower() -> 把字母转成小写形式.
                    print("谢谢您的使用，期待下次再会")
                    self.save_student()
                    break
            else:
                print("不合法操作，请重新输入")
