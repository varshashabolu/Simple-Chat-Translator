import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024)
            broadcast(msg, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen()

print("Server running on port 5555...")

while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    print(f"Connection from {addr}")
    threading.Thread(target=handle_client, args=(client_socket,)).start()
