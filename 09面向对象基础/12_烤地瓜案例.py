"""
案例：烤地瓜
"""


class SweetPopato:
    def __init__(self):
        self.cook_time = 0
        self.cook_status = '生的'
        self.condiment = []

    def __str__(self):
        return f"烘烤时间：{self.cook_time},烘烤状态：{self.cook_status},调料：{self.condiment}"

    def cook(self,time):
        if time < 0:
            print("时间是不合法值")
        else:
            self.cook_time += time
            if 0 <= self.cook_time < 3:
                self.cook_status = '生的'
            elif 3 <= self.cook_time < 7:
                self.cook_status = '半生不熟'
            elif 7 <= self.cook_time < 12:
                self.cook_status = '熟了'
            else:
                self.cook_status = '已烤焦，糊了'

    def add_condiment(self,condiment):
        self.condiment.append(condiment)


if __name__ == '__main__':
    sweet_popato = SweetPopato()
    sweet_popato.cook(3)
    sweet_popato.cook(4)
    sweet_popato.add_condiment("盐")
    sweet_popato.add_condiment("辣椒")
    print(sweet_popato)