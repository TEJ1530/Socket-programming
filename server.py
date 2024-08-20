import socket
import os
import ssl

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
name=socket.gethostname()
ip=socket.gethostbyname(name)
print(ip)

server_address = (ip, 8000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is up and running on port', server_address[1])

while True:
    # Wait for a connection
    print('Waiting for a client to connect...')
    client_socket, client_address = server_socket.accept()

    try:
        print('Connection from', client_address)

        # Receive the user's requested file name from the client
        data = client_socket.recv(1024).decode()
        file_name = data.split("/")[-1]

        # Check if the requested file exists
        if os.path.isfile(os.path.join('images', file_name)):
            # Open the file
            with open(os.path.join('images', file_name), 'rb') as f:
                file_data = f.read()

            # Send the file data to the client
            client_socket.sendall(file_data)
        else:
            # Send an error message to the client
            client_socket.sendall("File not found.".encode())

    finally:
        # Close the connection
        client_socket.close()
