


import time
import multiprocessing

def work():
    for i in range(1,10):
        print("正在努力工作中..")
        time.sleep(0.2)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work,name="work")
    print(f"p1进程的名字{p1.name}")
    # p1.daemon = True   # 设置守护进程
    p1.start()


    p1.terminate()
    time.sleep(1)
    print("main进程结束了..")
