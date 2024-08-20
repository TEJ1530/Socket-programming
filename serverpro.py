import socket
import os

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
        
        # Get a list of image files in the directory
        image_files = os.listdir('images')
        
        # Loop through the image files and send them to the client
        for image_file in image_files:
            # Open the image file
            with open(os.path.join('images', image_file), 'rb') as f:
                image_data = f.read()

            # Send the image data to the client
            client_socket.sendall(image_data)
        
    finally:
        # Close the connection
        client_socket.close()
