

# 可以捕获多个异常,但是无法区分
try:
    open("asdfdadf","r")
except (ZeroDivisionError,FileNotFoundError) as e:
    print("有异常了,异常是",e)

# 捕获多个异常同时区分
try:
    open("asdfdadadfaf","r")
except FileNotFoundError as e:
    print("文件没找到",e)
except ZeroDivisionError as e:
    print("除以0异常",e)