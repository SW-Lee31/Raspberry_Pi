from socket import *

HOST = ""
PORT = 5055
BUF_SIZE = 1024

servSocket = socket(AF_INET, SOCK_STREAM)
servSocket.bind((HOST, PORT))
servSocket.listen(5)
print("서버 대기 중")

conn, addr = servSocket.accept()
print("접속 소켓 정보 : ", addr)

while True:
    try:
        data = conn.recv(BUF_SIZE)
        if not data:
            break
        conn.sendall(data)
        conn.close()
    except Exception as e:
        print(e)
        break;


servSocket.close()
