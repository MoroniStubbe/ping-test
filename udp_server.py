import time
import socket

port = int('5000' + input('port: 5000'))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', port))

while True:
    message, address = server_socket.recvfrom(32)
    message = bytes(str(time.time()), 'utf-8')
    server_socket.sendto(message, address)