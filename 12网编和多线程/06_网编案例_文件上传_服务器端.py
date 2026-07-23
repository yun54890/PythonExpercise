

import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('127.0.0.100',10082))

server_socket.listen(5)
print("服务器启动，等待连接...")
accept_socket,client_info = server_socket.accept()
print(f"客户端 {client_info} 已连接")
# 读取客户端上传的文件数据
with open('./data/my.txt','wb') as f:
    while True:
        document = accept_socket.recv(8192)
        # 无数据时使客户端断开连接
        if not document:
            break
        f.write(document)

accept_socket.send("上传成功！".encode('utf-8'))
accept_socket.close()
server_socket.close()
print("文件接收完毕")