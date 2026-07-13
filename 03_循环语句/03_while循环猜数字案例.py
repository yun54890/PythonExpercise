

import random
random_num = random.randint(1,10)

num = 1
while num <= 3:
    final =  int(input("输入第%s次猜测的数字:" % num))
    if final != random_num:
        if final > random_num:
            print("猜大了")
        else:
            print("猜小了")
    else:
        print("猜对了")
        break
    num +=1