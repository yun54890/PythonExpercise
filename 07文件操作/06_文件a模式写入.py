

"""
a模式 append追加
- 文件不存在则新建
- 文件存在，则在原有内容之后继续写入（原有内容保留，反之w模式是原有内容清空）
"""

# 打开
f = open("hi.txt","a",encoding="utf-8")
f.write("\n")
f.write("Hello World\n")
f.write("Hello World\n")
f.write("Hello World\n")

# 关闭
f.close()