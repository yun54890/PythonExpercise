"""
案例： 演示多线程共享全局变量, 可能出现的问题

多线程共享全局变量, 出现问题的问题:
    累加次数
产生原因：
    线程1还没有来记得执行完(一个完整的动作)前, 被线程2抢走了资源,就可能出问题
"""

import threading


global_sum = 0

def func_one():
    global global_sum
    for i in range(10000000):
        global_sum += i
    print(f"func_one函数的sum：:{global_sum}")

def func_two():
    global global_sum
    for i in range(10000000):
        global_sum += i
    print(f"func_tow函数的sum：:{global_sum}")



if __name__ == '__main__':
    t1 = threading.Thread(target=func_one)
    t2 = threading.Thread(target=func_two)
    t1.start()
    t2.start()