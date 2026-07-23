"""
案例：网编入门案例, 服务器端给客户端发送消息,客户端给出回执消息

服务器开发流程：
    1. 创建服务器端Socket对象
    2. 连接服务器端,指定：服务器端IP,端口号
    3. 接收服务器端的信息并打印.
    4. 给服务器端发送消息
    5. 释放资源

# 细节
    客户端和服务端是通过 字节流(bytes) 的形式实现的
"""


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.100', 10080))

data = client_socket.recv(1024).decode('utf-8')
print(data)

client_socket.send('客户端发送的信息'.encode('utf-8'))

client_socket.close()