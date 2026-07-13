"""
使用f_format 方式格式化 （字符串拼接） 字符串
"""

name = "周杰伦"
age = 11
height = 172.55

# 1. 字符串之前写f标记,如f""
# 2. 变量用{}抱起来即可
message = f"我是{name},今年{age}岁，身高{height:.1f}厘米"
print(message)