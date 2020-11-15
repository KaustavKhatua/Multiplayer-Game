#!/usr/bin/env python3

import socket
# import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # for i in range(4):
    while True:
        # time.sleep(2)
        s.sendall(b'Hello, world')
        # data = s.recv(1024)
        # print(data.decode("utf-8"))

# print('Received', repr(data))