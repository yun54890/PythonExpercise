
def my_len(data):
    length = 0
    for i in data:
        length += 1
    return length

name = 'itheima'
print(f"{name}的长度是：{my_len(name)}")

info = "我爱学习，学习使我快乐"
print(f"{name}的长度是：{my_len(info)}")

# name = 'itheima'
# length = 0
# for i in name:
#     length += 1
# print(f"{name}的长度是：{length}")
#
# info = "我爱学习，学习使我快乐"
# length = 0
# for i in info:
#     length += 1
# print(f"{name}的长度是：{length}")