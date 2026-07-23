


import threading

def coding(name,num):
    for i in range(1,num+1):
        print(f"{name}正在敲第{i}遍 代码...")

def music(name,count):
    for i in range(1,count+1):
        print(f"{name}正在听第{i}首音乐")

if __name__ == '__main__':
    t1 = threading.Thread(target=coding,args=("小明",10))
    t2 = threading.Thread(target=music,kwargs={'name':'小美','count':10})
    t1.start()
    t2.start()