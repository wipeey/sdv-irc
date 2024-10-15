#!/bin/python3
import socket
import threading

# Print the received messages from the server
def receive_messages(s):
    while True:
        data = s.recv(1024)
        if not data:
            print("Connection lost!")
            break
        else:
            print(data.decode())


# Send a message to the server
def send_messages(s):
    while True:
        to_send = input()
        s.send(to_send.encode())


# Connect to the server and start listening for messages
def main():
    host = 'localhost'
    port = 1234

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.connect((host, port))
    except OSError:
        print(f'Unable to connect to {host}:{port}. Exiting...')
        exit(1)
    except ConnectionRefusedError:
        print(f'Connection to {host}:{port} refused. Exiting...')
        exit(1)

    send_msg = threading.Thread(target=send_messages, args=(s,))
    recv_msg = threading.Thread(target=receive_messages, args=(s,))

    send_msg.start()
    recv_msg.start()


if __name__ == '__main__':
    main()
