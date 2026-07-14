
t1 = ((1,2,3),(4,5,6))
# 报错TypeError: 'tuple' object does not support item assignment
# t1[0][0] = 0
# 报错 AttributeError: 'tuple' object has no attribute 'append'
# t1.append(5)

# 可以修改元组内部list的内部值
t1 = (1,2,[6,7,8])
t1[2][0] = 5           # 这是对元组内的list的某个元素进行重新赋值
t1[2][1] = 6
t1[2][2] = 7
print(t1)

# 这是对元组元素的重新赋值为新list,不支持
# t1[2]=[1,2,3]