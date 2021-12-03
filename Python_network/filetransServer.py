import socket

HOST = ""
PORT = 5055
BUF_SZ = 1024

s = socket.socket()
s.bind((HOST, PORT))
s.listen(5)
print("서버 대기 중")

while True:
    conn, addr = s.accept()
    print("접속 정보 : ", addr)
    data = conn.recv(BUF_SZ)
    print("메시지 : ", data)

    fileName = "/home/pi/Project_211201/testFileSender.txt" # 파일 경로
    f= open(fileName, "rb")
    fileData = f.read(BUF_SZ)

    while fileData:
        conn.send(fileData)
        fileData = f.read(BUF_SZ)
    f.close()
    print("파일 전송 완료")
    conn.close()
