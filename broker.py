import socket
import threading

# Create a socket for the broker
broker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
broker_host = 'localhost'  # Broker's IP address
broker_port = 12345  # Broker's port

# Bind the socket to the host and port
broker_socket.bind((broker_host, broker_port))

# Listen for incoming connections
broker_socket.listen(2)
print("Broker is listening for connections...")

# Store client sockets
clients = []

# Forward messages from sender to receiver
def forward_messages(sender, receiver):
    while True:
        try:
            message = sender.recv(1024)
            if not message:
                break
            receiver.send(message)
        except:
            break

# Accept incoming connections from sender and receiver
while True:
    try:
        client_socket, client_address = broker_socket.accept()
        clients.append(client_socket)

        if len(clients) == 2:
            print("Both Sender and Receiver connected.")
            sender_thread = threading.Thread(target=forward_messages, args=(clients[0], clients[1]))
            receiver_thread = threading.Thread(target=forward_messages, args=(clients[1], clients[0]))

            sender_thread.start()
            receiver_thread.start()
    except:
        break
