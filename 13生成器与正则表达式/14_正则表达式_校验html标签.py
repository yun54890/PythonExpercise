


import re


# html_str = '<html>我是html页面</html>'
# # copy
# # result = re.match(r'<[a-zA-Z]{1,4}>.*</[a-zA-Z]{1,4}>',html_str)
#
# # 分组
# result = re.match(r'<([a-zA-Z]{1,4})>(.*)</\1>',html_str)
#
# if result:
#     print(result.group())
# else:
#     print("未匹配！")




html_str = '<html><h1>我是html页面</h1></html>'

# result = re.match(r'<([a-zA-Z]{1,4})><(h[1-6])>.*</\2></\1>',html_str)
result = re.match(r'<(?P<A>[a-zA-Z]{1,4})><(?P<B>h[1-6])>.*</(?P=B)></(?P=A)>',html_str)


if result:
    print(result.group())
else:
    print("未匹配!")