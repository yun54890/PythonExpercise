"""
符号：{}
类型名：set
"""

# 字面量
{1,3,5,"哈哈",True,3,5}

# 变量
set1 = {1,3,5,"哈哈",True,3,5}

set2 = set()

print(set1,type(set1))
print(set2,type(set2))

# 去重切无序
set3 = {"bbb","bbb","aaa","ccc"}
print(set3,type(set3))

# 下标访问，报错，无法使用
print(set3[0])