import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 12345)

server_socket.bind(server_address)


server_socket.listen(1)
print("Server is waiting for a connection...")


client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
   
    message = client_socket.recv(1024).decode('utf-8')
    if not message:
        break

    print(f"Client: {message}")

    # Send a response
    response = input("You: ")
    client_socket.send(response.encode('utf-8'))

# Close the sockets
client_socket.close()
server_socket.close()
