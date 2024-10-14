#!/bin/python3
import socket
import threading
from time import sleep

# Server informations
host = 'localhost'
port = 1234

connected_clients = []

# Executes whenever a client connects to the server
def handle_client(conn, addr):
    global connected_clients

    client_ip = addr[0]
    client_port = addr[1]

    with conn:
        broadcast_message(f'{client_ip}:{client_port} connected to the server'.encode(), conn)

        while True:
            data = conn.recv(1024)
            if not data:
                broadcast_message(f'{client_ip}:{client_port} disconnected'.encode())
                try:
                    connected_clients.remove(conn) # Remove the client from the list
                    break
                except Exception:
                    pass
            else:
                broadcast_message(data, conn)


# Send a message to all connected clients except the sender
def broadcast_message(message, sender=None):
    global connected_clients

    print(message.decode()) # Log the received message to the console

    for client in connected_clients:
        try:
            if client != sender:  # Don't send the message to the sender
                client.send(message)
                # print(f'Sent message to client {client[1]}')
        except:
            connected_clients.remove(client)


# Return the current number of connected clients to the server
def get_connected_amount():
    global connected_clients
    return len(connected_clients)

 
 # Server loop that listens for new connections and handles them
def main():
    global connected_clients

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # SO_REUSEADDR allows the port to be reused after the server is stopped and restarted
    s.bind((host, port))

    print(f'Server started on {host}:{port}')

    while True:
        s.listen()

        conn, addr = s.accept()

        connected_clients.append(conn)
        print(get_connected_amount(), 'clients connected') # DEBUG

        connection_thread = threading.Thread(target=handle_client, args=(conn, addr))
        connection_thread.start()
    


if __name__ == '__main__':
    main()