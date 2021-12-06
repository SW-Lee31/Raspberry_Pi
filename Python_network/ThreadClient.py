# 1대n 통신을 위한 Client
import socket, threading

HOST = "192.168.0.57"
PORT = 5050
FM = "utf-8"

def send(uname):
    while True:
        msg = input("\nMe > ")
        data = uname + ">" + msg
        clientSocket.send(data.encode(FM))

def receive():
    while True:
        data = clientSocket.recv(1024).decode(FM)
        print("\n수신 : " + str(data))

if __name__ == "__main__":
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        uname = input("ID 입력 > ")
        clientSocket.connect((HOST, PORT))
        print("TCP 서버 접속시도")

        thread_send = threading.Thread(target=send, args=[uname])
        thread_send.start()

        thread_recv = threading.Thread(target=receive)
        thread_recv.start()
    except KeyboardInterrupt:
        clientSocket.close()
    
    
