import re

def test_pattern(pattern, s):
    res = re.match(pattern, s)
    # bool() 匹配成功=True，None=False
    print(f"字符串「{s}」 是否匹配：{bool(res)}")

# 使用示例
# test_pattern(r'.+hm.*', 'abchm')
# test_pattern(r'.?hm.*', 'abchm123')
# test_pattern(r'\d{3}hm\w{2,5}', '123hm12')

print("===== 第一组：.+hm.* 练习 =====")
p1 = r'.+hm.*'
test_pattern(p1, 'abchm')     # 成功
test_pattern(p1, 'hm123')     # 失败
test_pattern(p1, 'x99hmabc')  # 成功
test_pattern(p1, 'ahm')       # 成功

print("\n===== 第二组：.?hm.* 练习 =====")
p2 = r'.?hm.*'
test_pattern(p2, 'ahm123')    # 成功
test_pattern(p2, 'hm123')     # 成功
test_pattern(p2, 'abchm123')  # 失败
test_pattern(p2, 'xhm')       # 成功
test_pattern(p2, 'xyhm')      # 失败

print("\n===== 第三组：\\d{3}hm\\w{2,5} 练习 =====")
p3 = r'\d{3}hm\w{2,5}'
test_pattern(p3, '123hm123')   # 成功
test_pattern(p3, '1234hm123') # 失败
test_pattern(p3, '12hm123')   # 失败
test_pattern(p3, '123hmab')   # 成功
test_pattern(p3, '123hma')    # 失败 （\w只有1个）
test_pattern(p3, '123hm123456')#成功（只读取前5个\w，后面忽略）

print("\n===== 第四组：.*hm.* 拓展对比 =====")
p4 = r'.*hm.*'
test_pattern(p4, 'hm')        # 成功
test_pattern(p4, 'a1b2hmxyz')# 成功
test_pattern(p4, 'abc123')    # 失败（没有hm）