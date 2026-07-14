"""
列表本质上是一个类，内部提供了很多内置函数（称之为方法）
这些内置函数（方法）的使用，在语法上比较特殊需要写为：
列表变量.内置函数()
"""
from Tools.scripts.verify_ensurepip_wheels import print_notice

# 查找元素是否在列表中
# 列表变量.index(被查找的数据)
# 找到了返回下标值, 找不到报错
lst = ['itcast','itheima','python','666']
print(lst.index('python'))

# 快捷操作 确定某个元素是否在列表内
# 元素 in 列表变量
# 在里面给True  不在里面给False
print('666' in lst)
print('123123' in lst)

# 修改特定位置（索引）的元素值
# 语法：列表[下标]=值

# 正向下标
my_list = [1,2,3]
print("修改之前")
print(my_list)
print("修改之后")
my_list[0] = 5
print(my_list)

# 反向下标
my_list1 = [1,2,3,4,5]
print("修改之前")
print(my_list1)
print("修改之后")
my_list1[-1] = 1000
print(my_list1)


# 在列表指定下标位置，插入新元素
# 语法： 列表变量.insert(下标,元素)
# 当下标值超出列表的索引范围，则相当于在尾部新增一个元素
my_list2 = [1,2,3,4,5]
my_list2.insert(1,"ithema")
print(my_list2)


# 在列表尾部新增一个元素
# 语法： 列表变量.append(元素)
lst5 = [1,2,3]
lst5.append("ithema")
lst5.append("8997")
print(lst5)


# 在列表尾部新增一批元素（将其他数据容器追加到当前列表尾部）
# 语法： 列表变量.extend(数据容器)
lst6 = [1,2,3]
lst6.extend(lst5)
print(lst6)

# 删除列表元素
# 方式1 del 列表[下标]
lst6 = [1,2,3,4,5]
del lst6[1]
print(lst6)
# 方式2 列表.pop(下标)
# 和方式1的区别是 pop有返回值,返回的是: 被删除的元素
deleted_data = lst6.pop(1)
print(deleted_data)
print(lst6)

# 删除某元素在列表中的```第一个``` 匹配项
# 语法: 列表.remove(元素)
lst7 = ["itcast","itheima","python","666"]
lst7.remove("python")
print(lst7)
# lst7.remove("XXX")  # 如果元素不存在,则报错
# print(lst7)

# 清空列表
# 语法: 列表.clear()
lst8 = [1,2,3,4,5,6]
lst8.clear()
print(lst8)
# 方式2
list8 = [1,2,3,4,5,6]
list8 = []
print(list8)


# 统计列表内某个元素的个数
# 语法: 列表.count(元素)
lst9 = ["itcast","itheima","python","666","python"]
print(lst9.count("python"))

# 统计列表总共有多少元素
# 语法: len(列表)
lst10 =["itcast","itheima","python","666","python"]
print(len(lst10))