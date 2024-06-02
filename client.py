#!/usr/bin/python

import socket

serverName = "localhost"
serverPort = 3000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

path = input("path: ")
clientSocket.send(f"GET {path} HTTP/1.1".encode())
get = clientSocket.recv(4096)
print(get.decode())
clientSocket.close()
