"""
    ^ 表示开头
    $ 表示结尾
"""


import re

result = re.match(r'\d+.*','abc123xyz')      # 未匹配
print(result.group() if result else "未匹配")
result = re.search(r'\d+.*','abc123xyz')    # 123xyz
print(result.group() if result else "未匹配")
print("-"*50)

result = re.match(r'^\d+.*','abc123xyz')        # 未匹配
print(result.group() if result else "未匹配")
result = re.search(r'^\d+.*','abc123xyz')       # 未匹配
print(result.group() if result else "未匹配")
print("-"*50)


result = re.search(r'^\d+.*[a-zA-Z]{3}','abc123xyz123')    # 未匹配
print(result.group() if result else "未匹配")
result = re.search(r'^\d+.*[a-zA-Z]{3}','123你好xyz12')     # 123你好xyz
print(result.group() if result else "未匹配")
result = re.search(r'^\d+.*[a-zA-Z]{3}$','123你好xyz123')     # 未匹配
print(result.group() if result else "未匹配")
result = re.search(r'^\d+.*[a-zA-Z]{3}$','123你好xyz')     # 123你好xyz
print(result.group() if result else "未匹配")
print("-"*50)

# 校验手机号
# 规则： 1. 长度必须是11位    2. 必须是纯数字   3. 第1位数字必须是1  4. 第2位数字可以是3-9
result = re.search(r'^1[3-9]\d{9}$','18012341234')
print(result.group() if result else "未匹配")