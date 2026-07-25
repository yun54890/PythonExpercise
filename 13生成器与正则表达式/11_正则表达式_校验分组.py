"""
|          代表 或者的意思
()         代表 分组, 从左往右数, 第几个左小括号(, 就表示第几组
\sum       代表 引用第几组额内容
"""


import re

fruits = ['apple','banana','orange','pear']


for fruit in fruits:
    if re.match(r'apple|pear',fruit):
        print(fruit)
    else:
        print(fruit)