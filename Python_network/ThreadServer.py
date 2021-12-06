# 1대n 통신을 위한 Server
import socket, threading

HOST = ""
PORT = 5050

def acceptClient():
    while True:
        clientSocket, clientAddr = serverSocket.accept()
        print("클라이언트 접속 : ", clientSocket)
        print("접속 정보 : ", clientAddr)

        connectLst.append(clientSocket)
        thread_client = threading.Thread(target=broadcastUser, args=[clientSocket])
        thread_client.start()


def broadcastUser(clientSocket):
    while True:
        try:
            data = clientSocket.recv(1024)

            if data:
                bUser(clientSocket, data)
        except Exception as e:
            print(e)
            #break

# 메시지를 보내는 함수
def bUser(csSocket, msg):
    for client in connectLst:
        if client != csSocket: # 자신에게는 보내지 않음
            client.send(msg)


if __name__ == "__main__":
    try:
        connectLst = []
    
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind((HOST, PORT))
        serverSocket.listen(5)
        print("서버 대기중")
    
        threadServer = threading.Thread(target=acceptClient)
        threadServer.start()
    except KeyboardInterrupt:
        connectLst.clear()
        serverSocket.close()
        

    
