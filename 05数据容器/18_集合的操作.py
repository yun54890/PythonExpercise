"""
集合可以修改，有一些操作方法
"""

my_set = {"c","a","b","c"}
my_set.add("d")
print(my_set)

# remove(元素) 移除指定元素
my_set.remove("d")
print(my_set)

# pop() 随机取出一个元素返回，此元素在集合内被删除
print(my_set.pop())
print(my_set)

# 清空集合
my_set.clear()
print(my_set)

# 2个集合的差集
set1 = {1,2,3}
set2 = {1,4,5}
# 集合1.difference(集合2) 取差集（集合1而集合2没有的）
# 结果是组成一个新集合返回，原有的集合1和2不变
set3 = set1.difference(set2)
print("差集",set3)
print("原有set1",set1)
print("原有set2",set2)

print("-"*20)
# 2个集合的差集消除
# set1.difference_update(set2)
# 在set1内，删除和set2相同的元素
# 结果：set1被修改，set2不变
set1.difference_update(set2)
print("原有set1",set1)
print("原有set2",set2)

print("-"*20)
# 2个集合的并集，合并
# set1.union(set2) 2个集合合并为1个
# 结果：原有set1,set2不变，得到新的集合
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(set3)

my_set = {1,2,3,4,5,6,7,8,9,10}
# 统计元素数量， len(集合)
print(len(my_set))

print("-"*20)
my_set = {"c","a","b","c"}
# 遍历集合： 只可以用for,因为不支持下标
for i in my_set:
    print(i)   # 不确定顺序

# 混装集合
my_set = {1,2,3,4,5,6,7,8,9,10,"a","b","c"}
print(my_set)