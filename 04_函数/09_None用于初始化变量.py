


# 定义变量初始化 让变量设置全局(作用域是全局)
age = None
for i in range(5):
    age = int(input("你的年龄"))
    print(f"age:{age}")

print(f"最后一个同学的年龄是：{age}")