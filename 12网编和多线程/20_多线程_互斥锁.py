"""
案例： 演示多线程共享全局变量, 可能出现的问题

多线程共享全局变量, 出现问题的问题:
    累加次数
产生原因：
    线程1还没有来记得执行完(一个完整的动作)前, 被线程2抢走了资源,就可能出问题
解决方案:
    加锁思想, 即： 互斥锁
细节：
    使用互斥锁的时候, 要在合适的时机释放锁, 否则可能出现 死锁 或者 锁不住的情况
"""

import threading


global_sum = 0
mutex = threading.Lock()

def func_one():
    mutex.acquire()
    global global_sum
    for i in range(1000000):
        global_sum += 1
    print(f"func_one函数的sum：:{global_sum}")
    mutex.release()

def func_two():
    mutex.acquire()
    global global_sum
    for i in range(1000000):
        global_sum += 1
    print(f"func_tow函数的sum：:{global_sum}")
    mutex.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=func_one)
    t2 = threading.Thread(target=func_two)
    t1.start()
    t2.start()