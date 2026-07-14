

# 通用操作： 遍历： 略
# 通用操作： 求元素个数： len(数据容器) 略


lst = [1,2,3,4,5,6]
t = (1,2,3,4,56)
s_str = "itheima"
s_set = (1,2,3,4,5)
d = {"1":11,"2":2,"3":3,"4":4,"5":5}

# 找出最大值
print(f"{lst},max:{max(lst)}")
print(f"{t},max:{max(t)}")
print(f"{s_str},max:{max(s_str)}")
print(f"{s_set},max:{max(s_set)}")
print(f"{d},max:{max(d)}")

# 找出最小值
print("-"*20)
print(f"{lst},min:{max(lst)}")
print(f"{lst},min:{min(lst)}")
print(f"{t},min:{min(t)}")
print(f"{s_str},min:{min(s_str)}")
print(f"{s_set},min:{min(s_set)}")
print(f"{d},min:{min(d)}")


# 转列表
print("-"*20)
print(f"{t} 转list: {list(t)}")
print(f"{s_set} 转list: {list(s_set)}")
print(f"{s_str} 转list: {list(s_str)}")
print(f"{d} 转list: {list(d)}")      # 仅key转list

# 转元组
print("-"*20)
print(f"{lst} 转tuple: {tuple(lst)}")
print(f"{s_set} 转touple: {tuple(s_set)}")
print(f"{s_str} 转touple: {tuple(s_str)}")
print(f"{d} 转tuple: {tuple(d)}")      # 仅key转list