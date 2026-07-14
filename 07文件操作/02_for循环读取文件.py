

#  1. 打开  2读取  3关闭

f =open("hi.txt","r",encoding="utf-8")

# for line in f:
    # 处理\n 第一种方法
    # print(line,end="")

    # 处理\n 第二种方法
    # print(line.strip())


# 这个写法等同于下面的写法
for line in f.readlines():
    print(line.strip())


f.close()