import socket

s = socket.socket()
HOST = "192.168.0.57"
PORT = 5055
BUF_SZ = 1024

s.connect((HOST, PORT))
s.send(b"hello server")

with open("received_file", "wb") as f:
    print("file open")
    while True:
        data = s.recv(BUF_SZ)
        if not data:
            break
        f.write(data)

f.close()
s.close()
