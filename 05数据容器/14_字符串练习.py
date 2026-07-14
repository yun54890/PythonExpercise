

str = "itheima itcast boxuegu"

# 统计字符串内有多少个"it" 字符
sum =  str.count("it")
print(f"字符串itheima itcast boxuegu中有：{sum}个字符")
# 将字符串内的空格，全部替换为字符：“|”
new_str = str.replace(" ", "|")
print(f"字符串itheima itcast boxuegu,被替换空格后，结果：{new_str}")
# 按照 “|” 进行字符串分割，得到列表
new_list = str.split(" ")
print(f"字符串itheima itcast boxuegu,按照|分隔后，得到{new_list}")