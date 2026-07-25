

import re

s = 'qq:123456'


result = re.match(r'^(qq):(\d{6,12})$',s)

if result:
    print(result.group())
    print(result.group(0))  # 效果如上
    print("-"*30)
    print(result.group(1))
    print(result.group(2))
else:
    print("未匹配")