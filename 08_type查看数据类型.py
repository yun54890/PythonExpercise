"""
通过type语句查看字面量和变量的数据类型是什么
"""

# 语法:  type(被查看的)   被查看的可以是： 字面量、变量
# 执行顺序： 1. 先执行type(666)  2. 将结果通过print显示在屏幕上
print(type(66))
print(type(12.123))
print(type("ithema666"))


# 将类型信息记录到变量中
# 执行顺序： 1. 先执行type(666)得到结果  2.将结果赋值给左侧的变量int_type
int_type = type(66)
float_type = type(12.123)
str_type = type("ithema666")
print(int_type,float_type,str_type)