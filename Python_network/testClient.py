from socket import *
import sys

# 접속할 서버 주소, 포트
HOST = "192.168.0.57"
PORT = 5055 # 1 ~ 1024까지는 Well-Known 포트(시스템에서 활용하고 있을 가능성)
ADDR = (HOST, PORT)

# 소켓 : 가상의 네트워크를 통해 서로 간 연결

# 클라이언트 소켓 생성
# AF_INET : 네트워크 패밀리 정보
# SOCK_STREAM : 스트리밍 방식
clientSocket = socket(AF_INET, SOCK_STREAM)

# 서버생성
try:
    clientSocket.connect(ADDR)
    print("서버 접속 시도")
    clientSocket.close()
    print("클라이언트 종료")
except Exception as e:
    print("%s:%s" %ADDR)
    sys.exit()
