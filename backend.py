#!/bin/python3
import socket
import threading

# Function to receive messages from the server
def receive_messages(s, update_chat_callback):
    while True:
        try:
            data = s.recv(1024)
            if not data:
                update_chat_callback("Connection lost!")
                break
            else:
                update_chat_callback(data.decode())
        except ConnectionResetError:
            update_chat_callback("Server disconnected!")
            break

# Function to send messages to the server
def send_messages(s, message):
    try:
        s.send(message.encode())
    except Exception as e:
        print(f"Error sending message: {e}")

# Function to connect to the server
def connect_to_server(host='localhost', port=1234, update_chat_callback=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
    except (OSError, ConnectionRefusedError):
        if update_chat_callback:
            update_chat_callback(f"Unable to connect to {host}:{port}")
        return None

    if update_chat_callback:
        update_chat_callback(f"Connected to {host}:{port}")

    # Start a thread to listen for incoming messages
    recv_thread = threading.Thread(target=receive_messages, args=(s, update_chat_callback))
    recv_thread.start()

    return s  # Return the socket to be used in `client.py` for sending messages
