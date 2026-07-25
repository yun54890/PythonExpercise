

import re

s = '开心你就大声小，哈哈，呵呵，嘿嘿，零零，啦啦啦'

result = re.compile('哈|啦').sub('*',s)

print(result)
print("----------------")


result = re.sub('啦','*',s)
print(result)