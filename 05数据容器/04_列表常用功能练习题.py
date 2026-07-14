# 1. 定义列表，并用变量接收它
list = [21,25,21,23,22,20]

# 2. 追加一个数字31,到列表的尾部
list.append(31)
print(list)

# 3. 追加一个新列表[29,33,30]
list.extend([29,33,30])
print(list)

# 4. 取出第一个元素
delete_data = list.pop(0)
print(delete_data)
print(list)

# 5. 取出最后一个元素
delete_data = list.pop(-1)
print(delete_data)
print(list)

# 6. 查找元素31，在列表中的下标位置
print(list.index(31))