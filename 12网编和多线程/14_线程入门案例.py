


import threading

def coding():
    for i in range(10):
        print("正在敲第{i}遍 代码...")

def music():
    for i in range(10):
        print("正在听第{i}首音乐")

if __name__ == '__main__':
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)
    t1.start()
    t2.start()