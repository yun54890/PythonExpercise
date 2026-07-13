
number = 3

num = 3
if int(input("请输入第一次猜想的数字:")) == number:
    print("猜对了真棒")
elif int(input("不对，再重猜一次:")) == number:
    print("猜对了真棒")
elif int(input("不对，再猜最后一次:")) == number:
    print("猜对了真棒")
else:
    print("Sorry,全部猜错了，我想的是：%s" % number)