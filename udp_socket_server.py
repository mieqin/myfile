#udp_socket_server.py
from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)

server_addr = ('0.0.0.0',8000)

sockfd.bind(server_addr)

while True:
	data,addr = sockfd.recvfrom(1024)
	print("Recive message: %s,%s"%(data.decode(),addr))
	sockfd.sendto(b'Recive your message!',addr)
sockfd.close()