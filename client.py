import socket

def client():
   serverName = 'localhost'
   serverPort = 3000
   clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   clientSocket.connect((serverName, serverPort))
   masukan = input('input: ')
   clientSocket.send(masukan.encode())
   get = clientSocket.recv(4096)
   print(get.decode())
   clientSocket.close()
   
client()