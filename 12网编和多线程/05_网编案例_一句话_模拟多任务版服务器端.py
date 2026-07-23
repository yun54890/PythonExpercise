
import socket

# 创建
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定端口
server_socket.bind(('127.0.0.100',10080))

# 监听接口最大限量
server_socket.listen(5)

while True:
    try:
        # 等待客户端申请建立连接
        accept_socket,client_info = server_socket.accept()

        # 发送数据
        accept_socket.send('Welcome!'.encode('utf-8'))

        # 接收数据
        data = accept_socket.recv(1024).decode('utf-8')
        print(data)



        # 释放接口
        accept_socket.close()
    except:
        pass