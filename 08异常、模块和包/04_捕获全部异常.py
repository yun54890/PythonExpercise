
"""
需求: 不关系具体是什么异常,反正有问题就捕获掉
"""

try:
    # open("asafasdfad","r")
    1 / 0
except Exception as e:
    print("出问题了,问题是:",e)