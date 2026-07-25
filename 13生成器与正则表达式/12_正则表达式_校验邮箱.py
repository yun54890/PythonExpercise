

import re
email = "abc123@163.com"

result = re.search(r'^[a-zA-Z_0-9]{4,20}@(163|126|qq)\.com$',email)
print(result.group() if result else '邮箱不合法')