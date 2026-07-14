
lst = ["aa","bb",3,5,6]
# 取出来“bb”,3
print(lst[1:3:1])

# 取出来  5, 3,"bb"
print(lst[3:0:-1])

t = (1,3,5,7,9,11,13,15,17)
# 取出来 3 7
print(t[1:4:2])

# 取出来 15, 9, 3
print(t[-2:0:-3])

name = "itheima 666 and itcast"
# 反转字符串
print(name[::-1])