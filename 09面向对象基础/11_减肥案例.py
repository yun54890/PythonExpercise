



class Student:
    # 属性
    def __init__(self,weight,name):
        self.weight = weight
        self.name = name

    def __str__(self):
        return f"{self.name}同学当前体重是：{self.weight}KG"

    # def __del__(self):
    #     print(f"{self}删除了")
    # 行为

    def run(self):
        print("跑步一次，减少0.5kg")
        self.weight -= 0.5

    def eat(self):
        print("大吃大喝一次，增加2kg")
        self.weight += 2


if __name__ == '__main__':
    xiaoming = Student(100, "小明")
    xiaoming.run()
    xiaoming.eat()
    print(xiaoming)