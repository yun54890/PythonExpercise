

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.100', 10082))

with open('./test.txt','rb') as f:
    while True:
        data = f.read(8192)
        client_socket.send(data)
        if not data:
            break

client_socket.shutdown(socket.SHUT_WR)

data = client_socket.recv(8192).decode('utf-8')
print(data)


client_socket.close()