import socket

# Create a socket for the sender
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
broker_host = 'localhost'  # Broker's IP address
broker_port = 12345  # Broker's port

# Connect to the broker
sender_socket.connect((broker_host, broker_port))

while True:
    message = input("Enter a message to send (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    sender_socket.send(message.encode())

# Close the sender socket
sender_socket.close()
