"""
数据类型的转换
"""


# 数字转字符串
t1 = str(123123)
print(type(t1))

t2 = str(123123.123123)
print(type(t2))


# 整数与浮点数互转
print(float(123))
print(int(123.123))

# 字符串转数字
t3 = int("123")
print(type(t3))

# 错误示意
print(int("halkjf12321"))