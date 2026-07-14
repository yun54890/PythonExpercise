"""
文件操作模式：
- r 只读
- w 覆盖写
- a 追加写
- b 二进制处理

只有文本文件可以 r w a
非文本文件必须带有b,以二进制模式处理（读取01操作）
"""


# 打开
fr = open("D:/测试.mkv","rb")
fw = open("C:/测试.mkv","wb")

content = fr.read()
fw.write(content)

# 关闭
fr.close()
fw.close()