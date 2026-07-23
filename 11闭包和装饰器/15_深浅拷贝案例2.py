import copy

class Player:
    def __init__(self):
        self.inventory = ["剑","盾牌"]

    def get_inventory(self):
        # 危险写法! 直接返回了内部真实的 inventory 列表
        return self.inventory.copy()

p1 = Player()
my_bag = p1.get_inventory()
my_bag.append("加特林")
print(my_bag)

print(p1.get_inventory())
