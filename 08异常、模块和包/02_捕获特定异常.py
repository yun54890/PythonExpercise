"""
try:
    ...
except: 异常类型 as 变量:
    处理代码
可以针对特定的异常做捕获,如果出现的异常是我们所写的,则捕获成功,如果不是,则无法捕获
"""

# try:
#     1/0
# except ZeroDivisionError as e:
#     print("不能1/0")
#     print(e)


try:
    open("asd","r")    # FileNotFoundError
except ZeroDivisionError as e:   #捕获的是 ZeroDivisionError  会捕获失败
    print(e)