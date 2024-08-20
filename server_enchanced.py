import socket
import os


current_directory = os.path.abspath(os.getcwd())


image_directory = os.path.join(current_directory, 'server_images/')
video_directory = os.path.join(current_directory, 'server_videos/')
file_directory = os.path.join(current_directory, 'server_files/')


if not os.path.exists(image_directory):
    os.makedirs(image_directory)
if not os.path.exists(video_directory):
    os.makedirs(video_directory)
if not os.path.exists(file_directory):
    os.makedirs(file_directory)


server_ip = '192.168.1.6'
server_port = 12345


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((server_ip, server_port))


server_socket.listen(5)
print("Server is listening for incoming connections...")

while True:
  
    client_socket, client_addr = server_socket.accept()
    print("Connected to client: {}".format(client_addr))

    client_socket.sendall("Please select an option:\n1. View Images\n2. View Videos\n3. View Files\nEnter your choice (1/2/3): ".encode())
    choice = client_socket.recv(8192).decode()


    if choice == '1':
        items = os.listdir(image_directory)
    elif choice == '2':
        items = os.listdir(video_directory)
    elif choice == '3':
        items = os.listdir(file_directory)
    else:
        items = []

  
    item_list = "\n".join(items)
    client_socket.sendall(item_list.encode())

 
    file_name = client_socket.recv(8192).decode()


    if file_name in items:
        file_path = ""
        if choice == '1':
            file_path = os.path.join(image_directory, file_name)
        elif choice == '2':
            file_path = os.path.join(video_directory, file_name)
        elif choice == '3':
            file_path = os.path.join(file_directory, file_name)
        
        with open(file_path, 'rb') as file:
            file_data = file.read()
            client_socket.sendall(file_data)
    else:
        client_socket.sendall("File not found.".encode())

    client_socket.close()
