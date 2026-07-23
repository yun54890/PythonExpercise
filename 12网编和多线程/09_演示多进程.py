"""
案例：演示多进程入门案例

多进程目的：
    它属于多任务的一种实现方式, 目的是充分利用CPU资源, 提高程序执行效率

实现方式:
    1. 导包
    2. 创建进程对象, 关联目标函数
    3. 启动函数


"""

import time
import multiprocessing

def coding():
    for i in range(10):
        time.sleep(0.1)
        print(f"正在敲{i}段代码")

def listing():
    for i in range(10):
        time.sleep(0.1)
        print(f"正在听第{i}个歌曲......")

if __name__ == '__main__':
    # coding()
    # listing()

    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=listing)

    p2.start()
    p1.start()
