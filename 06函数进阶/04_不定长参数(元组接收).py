

def func(name,*xxx):
    """
    *是不定长参数的标记，表示收集全部参数到元组中
    :param name:
    :param xxx:
    :return:
    """
    print(f"我们是:{name},我们的成员有：")
    for i in xxx:
        print(i)

    print(type(xxx))
func("黑马天团","周杰伦","王力宏")


# 注意，语法上支持下列的函数参数传递写法，在实际调用的时候需要通过关键字传参给age提供值
# 否则传入的值会被不定长参数被收集
def func1(name,*xxx,age):
    """
    *是不定长参数的标记，表示收集全部参数到元组中
    :param name:
    :param xxx:
    :return:
    """
    print(f"我们是:{name},我们的成员有：")
    for i in xxx:
        print(i)

# 错误写法
# func1("黑马天团","周杰伦","王力宏",11)
# 正确写法
func1("黑马天团","周杰伦","王力宏",age=11)
