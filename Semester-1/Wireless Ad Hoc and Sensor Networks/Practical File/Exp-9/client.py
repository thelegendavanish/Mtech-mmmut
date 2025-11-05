# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Socket Programming - Persistent Client
# Description:
#   This program implements a TCP client that communicates continuously 
#   with the server until either side sends 'exit'.
# ------------------------------------------------------------------------------

import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

# Connect to server
client_socket.connect((host, port))
print(f"🔗 Connected to server {host}:{port}")

# Chat loop
while True:
    msg = input("You (Client): ")
    client_socket.send(msg.encode())

    if msg.lower() == 'exit':
        print("❌ Connection closed by client.")
        break

    data = client_socket.recv(1024).decode()
    print(f"\n📨 Server: {data}")

    if data.lower() == 'exit':
        print("❌ Server ended the chat.")
        break

# Close connection
client_socket.close()
print("🔒 Client shutdown successfully.")
