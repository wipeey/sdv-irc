#!/bin/python3
import socket

def main():
    host = 'localhost'
    port = 3301

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        to_send = input("Prompt: ")
        s.send(to_send.encode())
    


if __name__ == '__main__':
    main()