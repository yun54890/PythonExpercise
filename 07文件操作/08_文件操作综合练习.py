

# 打开
fr = open("bill.txt","r",encoding="utf-8")
fw = open("bill-back.txt","w",encoding="utf-8")

for line in fr:
    line = line.strip()    # 去除最后的\n和前后多余的空格
    if "测试" == line.split(",")[-1]:
        continue
    fw.write(line)
    fw.write("\n")
# 关闭
fr.close()
fw.close()
