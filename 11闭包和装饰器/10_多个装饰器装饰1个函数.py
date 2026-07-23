"""
案例：演示多个装饰器装饰1个函数

记忆：
    多个装饰器装饰1个原函数, 是按照 由内向外的顺序来装饰的
    但如果你要是用 装饰器的写法来做, 看到的效果是：从上往下执行的
"""

# 需求：发表评论前, 需要先登录, 在验证验证码, 请用所学, 模拟该功能


# 定义装饰器, 表示： 登录
def check_login(fn_name):
    def fn_inner():
        print("校验登录.....")
        fn_name()
    return fn_inner

# 定义装饰器, 表示： 验证验证码
def check_code(fn_name):
    def fn_inner():
        print("验证码验证...")
        fn_name()
    return fn_inner

# 定义原函数, 表示 发表评论
# @check_login
# @check_code
def comment():
    print("发表评论..")



if __name__ == "__main__":
    # 语法糖写法
    comment()
    print("-"*30)

    # 传统写法
    fn_inner = check_code(comment)
    fn_inner = check_login(fn_inner)
    fn_inner()