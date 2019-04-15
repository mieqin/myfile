#tcp_socket_client.py
from socket import *

sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

while True:
	data = input("Send message>>>")
	sockfd.send(data.encode())
	if data == "##":
		break
	data = sockfd.recv(1024)
	print(data.decode())

sockfd.close()