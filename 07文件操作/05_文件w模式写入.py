"""
mode:
- r 只读
- w 写入
    - 如果文件不存在则新建
    - 如果文件存在，则清空原有内容，写入新的
- a 追加
"""

# 打开文件
d = open("hiFirst.txt","w",encoding="utf-8")

# 将helloworld 写入文件
# write函数表示将内容写入到缓冲区
d.write("Hello World")

# 将缓冲区内的内容，写到硬盘（文件）中
d.flush()
# 关闭
d.close()