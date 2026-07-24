"""
案例：演示多线程特点

多线程特点：
    1. 线程执行具有随机性,原因是因为CPU在做着高效的切换
    2. 默认情况下,主线程会等待子线程结束再结束
    3. (同一个进程的)线程间 数据共享
    4. 多线程操作共享数据, 可能会出现安全问题, 可以用 互斥锁解决
"""

import time,threading

my_list = []

def wirte_data():
    for i in range(10):
        my_list.append(i)
        print("写入数据:",i)
    print(f'write_data函数:{my_list}')

def read_data():
    time.sleep(2)
    print(f'read_data函数:{my_list}')


if __name__ == '__main__':
    t1 = threading.Thread(target=wirte_data)
    t2 = threading.Thread(target=read_data)

    t1.start()
    t2.start()