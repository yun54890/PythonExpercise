"""

抽象类解释：
    概述：
        在python中，抽象类 = 接口， 即： 有抽象方法的类就是 抽象类，也叫 接口
        抽象方法 = 没有方法体的方法， 即： 方法体是 pass 修饰的
    作用/目的：
        抽象类一般充当父类，用于指定行业规范，准则，具体的实现交由 子类 来完成
"""


class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调核心制冷科技")

    def hot_wind(self):
        print("美的空调电热丝加热")

    def swing_l_r(self):
        print("美的空调无风感左右摆风")


class CREE_AC(AC):
    def cool_wind(self):
        print("格力空调变频省电制冷")

    def hot_wind(self):
        print("格力空调电热丝加热")

    def swing_l_r(self):
        print("格力空调静音左右摆风")

def make_cool(ac:AC):
    ac.cool_wind()

def hot_wind(ac:AC):
    ac.hot_wind()

def swing_l_r(ac:AC):
    ac.swing_l_r()

midea_ac = Midea_AC()
cree_ac = CREE_AC()

make_cool(midea_ac)

make_cool(cree_ac)
hot_wind(cree_ac)
swing_l_r(cree_ac)