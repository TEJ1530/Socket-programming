import socket
import threading
import pyaudio

# Define server address and port
SERVER_HOST = '192.168.1.8'
SERVER_PORT = 5002

# Define audio settings
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Initialize PyAudio object
audio = pyaudio.PyAudio()

# Create stream to record audio data
stream_in = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK_SIZE)

def send_audio():
    """
    Send audio data from this client to the server
    """
    while True:
        try:
            data = stream_in.read(CHUNK_SIZE)
            client_socket.sendall(data)
        except:
            break

def receive_audio():
    """
    Receive audio data from the server and play it
    """
    while True:
        try:
            data = client_socket.recv(CHUNK_SIZE)
            stream_out.write(data)
        except:
            break

# Create threads for sending and receiving audio data
send_thread = threading.Thread(target=send_audio)
receive_thread = threading.Thread(target=receive_audio)

# Start threads
send_thread.start()
receive_thread