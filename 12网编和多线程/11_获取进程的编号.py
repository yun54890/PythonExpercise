"""
案例： 演示获取进程的编号

进程的编号解释:
    概述：
        在设备中, 每个程序(进程)都有自己的唯一进程id, 当程序释放的时候, 该进程id也会释放, 即： 进程id是可以重复使用的
    目的:
        1. 查看子进程和父进程的关系, 方便管理
        2. 例如： 杀死指定进程,创建子进程
    格式：
        查看当前进程的pid:
            OS模块(operating, 系统模块) 的getpid()            get Process id
            multiprocessing#current_process()的pid属性
        查看当前进程的pid：         parent process id(父进程id)
            os#getppid()
"""

import os
import time
import multiprocessing

def coding(name,num):
    for i in range(1,num+1):
        time.sleep(0.1)
        print(f"{name} 正在敲第{i}行代码...")
    print(f"p1进程的pid:{os.getpid()},{multiprocessing.current_process().pid},父进程id(ppid为):{os.getppid()}")


def music(name,count):
    for i in range(1,count+1):
        time.sleep(0.1)
        print(f"{name} 正在听第{i}首歌...")
    print(f"p2进程的pid:{os.getpid()},{multiprocessing.current_process().pid},父进程id(ppid为):{os.getppid()}")


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=coding,args=('虚竹',10))
    p2 = multiprocessing.Process(target=music,kwargs={'count':10,'name':'刘备'})

    p1.start()
    p2.start()