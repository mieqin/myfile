#upd_broadcast_server.py
from socket import *

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#设置套接字地址重用
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#套接字绑定服务端地址
sockfd.bind(('0.0.0.0',9999))

while True:
	try:
		data,addr = sockfd.recvfrom(1024)
	except (KeyboardInterrupt, SyntaxError):
		raise
	except Exception as e:
		print(e)
	finally:
		print(data.decode())
	if data == '##':
		break
sockfd.close()