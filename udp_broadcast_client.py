#upd_broadcast_client.py
from socket import *
import time

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#设置套接字地址重用
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

addr = ('127.0.0.1',9999)

while True:
	time.sleep(1)
	data = input("Input your message:")
	sockfd.sendto(data.encode(),addr)
	if data == '##':
		break

sockfd.close()