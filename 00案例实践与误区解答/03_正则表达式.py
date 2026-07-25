

import re

# 需求： 在列表中["apple","banana","orange","pear"],匹配apple和pear
list = ['apple','banana','orange','pear']

for i in list:
    if re.match(r'apple|pear',i):
        print(i)

print("-"*30)

# 需求：匹配出163、126、qq等邮箱
email = '207140123@qq.com'
result = re.match(r'^[a-zA-Z0-9_]+@(163|126|qq)\.com$',email)
print(result.group())
print("-"*30)


# 需求：匹配qq:10567这样的数据,提取出来qq文字和qq号码
str = 'qq:10567'
result = re.match(r'(qq):(\d{5})',str)
print(result.group(1))
print(result.group(2))
print("-"*30)


str_one = '<html>hh</html>'
result = re.match(r'<([a-zA-Z]{1,4})>.*</\1>',str_one)
print(result.group())
print("-"*30)

str_two = '<html><h1>www.itcast.cn</h1></html>'
result = re.match(r'<(?P<A>[a-zA-Z]{1,4})><(?P<B>h[1-6])>(w{3})(\.)(.*)(\.cn)</(?P=B)></(?P=A)>',str_two)
print(result.group())