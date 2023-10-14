import socket

# Create a socket for the receiver
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
broker_host = 'localhost'  # Broker's IP address
broker_port = 12345  # Broker's port

# Connect to the broker
receiver_socket.connect((broker_host, broker_port))

while True:
    message = receiver_socket.recv(1024).decode()
    if not message:
        break
    print("Received:", message)

# Close the receiver socket
receiver_socket.close()
