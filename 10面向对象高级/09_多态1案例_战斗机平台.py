"""


需求：
    1. 构建对战平台(公共函数)object_paly,接收：英雄机 和 敌机
    2. 在不修改对话平台代码的情况下，完成多次战斗
    3. 规则：
        英雄机,1代战斗力60，2代战斗力80
        敌机，1代战斗力70


代码提示：
    英雄机1代 HeroFighter
    英雄机2代 AdvHeroFighter
    敌机 EnemyFighter
"""

# 英雄机1代 HeroFighter
class HeroFighter:
    def power(self):
        return 60

# 英雄机2代 AdvHeroFighter
class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80


# 敌机1代  EnemyFighter
class EnemyFighter:
    def power(self):
        return 70

# 构建对战平台，公共的函数，接收不同的参数，有不同的效果 -> 多态
def object_play(hero:HeroFighter,enemy:AdvHeroFighter):
    if hero.power() >= enemy.power():
        print("英雄机 战胜 敌机！")
    else:
        print("英雄机 惜败 敌机！")



if __name__ == "__main__":
    h1 = HeroFighter()
    h2 = AdvHeroFighter()
    e1 = EnemyFighter()
    object_play(h1,e1)
    object_play(h2,e1)