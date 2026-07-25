"""
案例：基于传入的数值(每批次的歌词条数), 创建 生成器, 生成批次歌词
"""
import math
def dataset_box(data_size):
    with open('./test.txt','r',encoding='utf-8') as f:
        lines = f.readlines()
        data_total = math.ceil(len(lines) / data_size)
        print(data_total)

        for idx in range(data_total):
            yield lines[data_size * idx: data_size * idx + data_size]

list = dataset_box(3)
print(next(list))
print(next(list))
for item in list:
    print(item)