"""


"""

print("欢迎来到黑马ATM")
name = input("请输入您的姓名：")
money = 5000000  # 初始余额

def menu():
    """
    ATM案例的主菜单函数，提示用户做输入，并返回用户输入的数字
    :return: 返回菜单栏操作的值
    """
    print("-"*20,"主菜单","-"*20)
    print(f"{name},您好,欢迎来到黑马ATM,请选择操作:")
    print(f"查询余额\t[输入1]")
    print(f"存款\t\t[输入2]")
    print(f"取款\t\t[输入3]")
    print(f"退出\t\t[输入4]")
    return int(input("请输入您的选择："))

def check_money(title):
    """
    查询余额
    :return: None
    """
    if title:
        print("-" * 20, "查询余额", "-" * 20)
    print(f"{name}您好，您的余额剩余：{money}元")


def take_money():
    """
    取款操作
    :return:None
    """
    global money
    print("-" * 20, "取款", "-" * 20)
    num = int(input(f"{name},您要取款多少元："))
    if num <= money:
        money -=num
        print(f"{name},您好，您取款{num}元成功")
        check_money(False)
    else:
        print(f"{name},您好,您的余额不足{num}元")
        check_money(False)

def save_money():
    """
    存款操作
    :return:None
    """
    global money
    print("-" * 20, "存款", "-" * 20)
    num = int(input(f"{name},您要存款多少钱："))
    money += num
    print(f"{name},您好，您存款{num}元成功")
    check_money(False)

while True:
    input_num = menu()
    if input_num == 1:
        check_money(True)
    elif input_num == 2:
        save_money()
    elif input_num == 3:
        take_money()
    elif input_num == 4:
        print("再见！")
        break
    else:
        print("非法操作，请重新输入")