"""
文件操作3大步
1. 打开
2. 读或写
3. 关闭
"""

# 相对路径写法 在文件所在的文件夹内寻找
f = open("hi.txt","r",encoding="utf-8")
# 绝对路径写法  在指定的路径中寻找
# f2 = open("D:/hi.txt","r",encoding="utf-8")

# content = f.read()   # 读取全部
# print(content)

# content = f.read(6)
# print(content)

lst = f.readlines()
print(lst)
print(type(lst))

f.close()