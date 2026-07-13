
# 需求： 身高大于120需要VIP级别大于3 可以免费， 身高小于等于120 直接免费

if int(input("请输入你的身高:")) > 120:
    if int(input("请输入你的VIP级别:")) > 3:
        print("免费（身高>120且VIP级别>3）")
    else:
        print("收费")
else:
    print("免费（身高<120）")