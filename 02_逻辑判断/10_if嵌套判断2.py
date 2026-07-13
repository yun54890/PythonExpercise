
age = int(input("请输入您的年龄："))
year = int(input("请输入您的入职时间："))
level = int(input("请输入你的级别:"))

if age >= 18:
    if age < 30:
        if year >= 2:
            print("发放礼物")
        elif level >= 3:
            print("发放礼物")
        else:
            print("不满足要求")
    else:
        print("成年了，但是年龄超标")
else:
    print("不满足要求")