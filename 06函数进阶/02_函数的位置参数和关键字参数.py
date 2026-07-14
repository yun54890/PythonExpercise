
def user_info(name,age,gender):
    print(f"我是{name}， 今年{age}岁 性别{gender}")


# 位置调用（位置参数） 要做到实参和形参 一一对应
user_info("小明",20,"男")

# 关键字调用（关键字参数）
# 语法: user_info(形参=实参,......)
user_info(name="小美",age=20,gender="女")
# 关键字参数顺序可以错乱，因为明确指定了 实参对应的形参
user_info(gender="女",name="小美",age=20)

# 混用
user_info("小青",gender="女",age=20)
# 如果混用，位置参数必须在关键字参数的左侧
# user_info(gender="男，11,name="周杰伦") 错误写法
user_info("小强",11,gender="男")
# 位置参数要注意  一一对应
user_info(11,"小强",gender="男")

