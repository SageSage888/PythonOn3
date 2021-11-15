import socket
import os
#s.system('ping 140.238.212.157')
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect(("127.0.0.1", 9696))


def start_client():
    while True:
        soc.send(input("print something ").encode('utf-8'))

        data = soc.recv(4096)
        print(data.decode("utf-8"))


if __name__ == '__main__':
    start_client()
