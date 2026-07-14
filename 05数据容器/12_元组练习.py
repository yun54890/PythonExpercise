
list = ("周杰伦",11,['football','music'])

# 查询其年龄所在的下标位置
print(list.index(11))

# 查询学生的姓名
print(list[0])

# 删除学生爱好中的football
# del list[2][0]
list[2].pop(0)
print(list)

# 增加爱好：coding到爱好list内
list[2].append("coding")
print(list)