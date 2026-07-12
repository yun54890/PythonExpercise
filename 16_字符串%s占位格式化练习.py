"""
字符串%s占位格式化练习
"""

money = 100000
name = "张三"
salary = 15000

info = "我是%s,钱包有%.2f元，但是今天发放了工资%.2f元，目前钱包有%.2f元" % (name, money, salary, money+salary)
print(info)