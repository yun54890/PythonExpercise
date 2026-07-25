







import re

result = re.match('.it', '\nit')

if result:
    print(result.group())
else:
    print("fail")