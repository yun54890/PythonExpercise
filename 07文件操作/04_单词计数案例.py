
sum = 0
#  打开文件
d = open("word.txt","r",encoding="utf-8")

for line in d:
    # 处理\n
    line = line.strip()
    # 方式1
    sum +=  line.count("itheima")
    
    # 方式2
    # 分隔空格输出
    # for word in line.split(" "):
    #     print(word)
    #     if word == "itheima":
    #         sum = sum + 1

# 关闭文件
d.close()

print(sum)