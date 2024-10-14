#!/bin/python3
import socket
import threading

def receive_messages(s):
    while True:
        data = s.recv(1024)
        if not data:
            print("Connection lost!")
            break
        else:
            print(data.decode())


def send_messages(s):
    while True:
        to_send = input("Prompt: ")
        s.send(to_send.encode())


def main():
    host = 'localhost'
    port = 3301

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    send_msg = threading.Thread(target=send_messages, args=(s))
    recv_msg = threading.Thread(target=receive_messages, args=(s))

    send_msg.start(); recv_msg.start()


if __name__ == '__main__':
    main()