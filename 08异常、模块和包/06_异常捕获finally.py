"""
有异常了,应该要怎么处理  用except抓
没有异常应该怎么处理     用else
不管有没有异常, 必做的事情  finally
"""

try:
    # 1/0
    print("hello")
except Exception as e:
    print("有问题",e)
else:
    print("一切正常")
finally:
    print("有没有问题,我都执行")