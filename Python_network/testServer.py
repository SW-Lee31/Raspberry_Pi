from socket import *

HOST = "" # 서버의 IP정보를 자동으로 설정받음
PORT = 5055
ADDR = (HOST, PORT)

# 서버 소켓 생성
serverSocket= socket(AF_INET, SOCK_STREAM)
print("서버 소켓 생성")
# 서버 주소를 서버소켓에 바인딩
serverSocket.bind(ADDR)
print("서버 주소 바인딩")
# 클라이언트에서 접속하도록 대기 listen(5) 대기 queue를 5로 설
serverSocket.listen(5)
print("서버 대기 중")
# 클라이언트 접속 허용
conn, addr_info = serverSocket.accept()
print("클라이언트 접속 허용")
# 클라이언트, 서버 소켓 종료
conn.close()
serverSocket.close()
print("서버 소켓, 클라이언트 종료")
