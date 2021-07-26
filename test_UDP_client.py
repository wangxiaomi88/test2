import socket
import time

ADDR=("127.0.0.1",8888)
sockfd=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg=input("请输入：")

    sockfd.sendto(msg.encode(),ADDR)


    if msg=="file":
        time.sleep(0.1)
        file_name = "fengjing.jpeg"
        f = open(file_name, "rb")
        while True:
            data = f.read(1024)
            sockfd.sendto(data,ADDR)
            time.sleep(0.01)
            if not data:
                break
        f.close()
        time.sleep(0.1)
        sockfd.sendto("#file".encode(), ADDR)

    data, addr = sockfd.recvfrom(1024)
    print(data.decode())

    if not msg:
        break

sockfd.close()