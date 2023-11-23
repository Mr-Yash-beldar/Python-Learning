import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 12345)


client_socket.connect(server_address)
print("Connected to the server.")

while True:
   
    message = input("You: ")
    client_socket.send(message.encode('utf-8'))

   
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server: {response}")

    if message.lower() == "exit":
        break

client_socket.close()
