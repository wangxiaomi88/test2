import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockfd.bind(("127.0.0.1", 8888))

while True:
    try:
        data, addr = sockfd.recvfrom(2048)

        if data == "file".encode():
            f = open("haha.jpeg", "wb")
            while True:
                data, addr = sockfd.recvfrom(2048)
                if data == "#file".encode():
                    break
                else:
                    f.write(data)

            f.close()



        print("连接到客户端{}，信息为：{}".format(addr,data.decode()))
        sockfd.sendto("好的".encode(),addr)
    except KeyboardInterrupt:
        break

sockfd.close()
