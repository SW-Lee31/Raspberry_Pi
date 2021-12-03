from socket import *

HOST = "192.168.0.57"
PORT = 5055
BUF_SIZE = 1024
str = "안녕하세요"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((HOST, PORT))

clientSocket.sendall(str.encode('utf-8'))
data = ((clientSocket.recv(BUF_SIZE)).decode('utf-8'))
print("데이터 수신 : " + data)
clientSocket.close()
