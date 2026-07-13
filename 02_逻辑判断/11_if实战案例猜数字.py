"""
定义一个数字（1~10，随机产生），通过3次判断来猜出来数字
"""

#  数字随机产生，范围1-10
import random
radndom_num = random.randint(1,10)

# 有3次机会猜测数字，通过3层嵌套判断实现
num = int(input("第一次输出猜测数字"))

if num == radndom_num:
    print("你真棒一次就猜对了")
else:
    if num > radndom_num:
        print("你猜大了")
    else:
        print("你猜小了")

    num = int(input("第二次输入猜测数字："))
    if num == radndom_num:
        print("真棒，二次就猜对了")
    else:
        if num > radndom_num:
            print("你猜大了")
        else:
            print("你猜小了")

        num = int(input("第三次输入猜测数字："))
        if num == radndom_num:
            print("真棒，三次就猜对了")
        else:
            print("机会用完，全部猜错了")

