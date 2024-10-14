#!/bin/python3
import socket
import threading
from time import sleep

# Server informations
host = 'localhost'
port = 1234


# Executes whenever a client connects to the server
def handle_client(conn, addr):
    client_ip = addr[0]
    client_port = addr[1]
    with conn:
        print(f'{client_ip}:{client_port} connected to the server')
        while True:
            data = conn.recv(1024)
            if not data:
                print(f'{client_ip}:{client_port} disconnected')
                break
            else:
                print(data.decode())


# Setting up listener
# Starting core threads
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    while True:
        s.listen()

        conn, addr = s.accept()

        connection_thread = threading.Thread(target=handle_client, args=(conn, addr))
        connection_thread.start()
    


if __name__ == '__main__':
    main()