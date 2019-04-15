#tcp_socket.py
from socket import *

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

#绑定服务端地址
sockfd.bind(ADDR)

#监听套接字
sockfd.listen(5)
print("等待连接......")
#连接客户端
connfd,addr = sockfd.accept()
print("服务端地址为：",addr)

while True:	
	#接收客户端数据
	data = connfd.recv(1024).decode()
	if data == '##':
		break
	print(data)
	
	n = connfd.send(b'Receive your message')
connfd.close()
sockfd.close()