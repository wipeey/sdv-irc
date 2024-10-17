#!/bin/python3
import socket
import threading

# TODO
# +> username for each user (username: message)
# +> connected_clients == dictionary (conn: username)

class ServerCommands:
    # Return the amount of connected clients as an integer
    @staticmethod
    def list_command(server):
        connected_amount = server.get_connected_amount()
        return f'There are {connected_amount} client(s) connected'

    # Kick a user from the chat (currently closes its connection)
    @staticmethod
    def kick_command(conn):
        connected_clients = server.connected_clients
        if conn in connected_clients:
            conn.send(b'You were kicked from the server')
            conn.close()

    command_handlers = {
        #'help': help_command,
        'list': list_command
        #'kick': kick_command,
    }


class ServerMain:
    def __init__(self, host='10.111.0.211', port=1234):
        # Server information
        self.host = host
        self.port = port
        self.connected_clients = []

    # Executes whenever a client connects to the server
    def handle_client(self, conn, addr):
        client_ip = addr[0]
        client_port = addr[1]

        with conn:
            self.broadcast_message(f'{client_ip}:{client_port} connected to the server'.encode(), conn)

            while True:
                data = conn.recv(1024)
                if not data: # Happens when the connection is closed
                    self.broadcast_message(f'{client_ip}:{client_port} disconnected'.encode())
                    try:
                        self.connected_clients.remove(conn) # Remove the client from the list
                        break
                    except Exception:
                        pass
                else:
                    self.broadcast_message(data, conn) # Send the data to all users


    # Send a message to all connected clients except the sender
    def broadcast_message(self, message, sender=None):
        print(message.decode()) # Log the received message to the console

        for client in self.connected_clients:
            try:
                if client != sender:  # Don't send the message to the sender
                    client.send(message)
                    # print(f'Sent message to client {client[1]}')
            except:
                self.connected_clients.remove(client)

    # Return the current number of connected clients to the server
    def get_connected_amount(self):
        return len(self.connected_clients)

    # Prompt for command executing
    def execute_command(self):
        while True:
            try:
                command = input()

                parts = command.split()
                base_command = parts[0].lower()
                args = parts[1:]

                # Using ServerCommands class to handle commands
                if base_command in ServerCommands.command_handlers:
                    result = ServerCommands.command_handlers[base_command](self)
                else:
                    result = (f'Unknown command {command}')
                
                print(result)
            except Exception as e:
                print(e)

    # Server loop that listens for new connections and handles them
    def main(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # SO_REUSEADDR allows the port to be reused after the server is stopped and restarted
        s.bind((self.host, self.port))

        print(f'Server started on {self.host}:{self.port}')

        send_command_thread = threading.Thread(target=self.execute_command)
        send_command_thread.start()

        while True:
            s.listen()
            conn, addr = s.accept()

            self.connected_clients.append(conn)
            # print(self.get_connected_amount(), 'clients connected')

            connection_thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            connection_thread.start()

# Main execution now creates an instance of ServerMain and runs it
if __name__ == '__main__':
    server = ServerMain()
    server.main()
