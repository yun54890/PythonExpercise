
# 字符串的下标操作，支持下标正向反向都支持
s = "itheima哈哈666"

print(s[7])
print(s[-1])

# 字符串的修改（不可改）
# s[-6] = "b"   # 这是修改字符串的值

s = "abc"        # 这是重新赋值变量
print(s)

# index   查找元素在容器内的下标，找到返回下标，找不到报错
s = "itheima哈哈666"
print(s.index("哈哈"))


# replace(old_str,new_str)
# 将字符串内的指定字符，替换为新的
# 字符串本身无法修改，所以replace函数是```返回```  一个新的修改后的字符串
# 并没有对原有字符串做出修改
s = "周杰伦|王力宏|刘德华"
s2 = s.replace("|",",")
print(s)
print(s2)

# split(分隔符) 可以按指定分隔符，将字符串分隔出多份，存入一个新list内并返回
s = "周杰伦|王力宏|刘德华"
lst = s.split("|")
print("分隔后：",lst,type(lst))
print("本身字符串：",s)

# strip()  去除字符串的前后空格和回车符
s = " \nitheima666\n"
# 原有字符串不会被修改，而是返回一个新的
s2 = s.strip()
print(s2)


# strip(字符串)  去除字符串中前后指定的字符  注意的是，只是清除字符串中的前后，中间不会进行清除
s = "|||ithe||ima666|||"
s2  = s.strip("|")
print(s2)
s3 = s.replace("|","")
print(s3)


# 统计字符串有多少个a
# count(字符串) 统计字符串内有多少个指定的字串
s = "itheima a a a a a"
num = s.count("a")
print(num)


# 统计字符串长度
# len(字符串)
s = "abc123您好&*"
num = len(s)
print(num)