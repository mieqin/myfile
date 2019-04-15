#udp_socket_client.py
from socket import *
import sys

sockfd = socket(AF_INET,SOCK_DGRAM)

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

while True:
	data = input("Input>>>")
	sockfd.sendto(data.encode(),ADDR)
	data,addr = sockfd.recvfrom(1024)
	print(data.decode())
sockfd.close()