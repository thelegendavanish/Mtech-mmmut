# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Socket Programming - Persistent Server
# Description:
#   This program implements a TCP server that communicates continuously 
#   with a connected client until either side sends 'exit'.
# ------------------------------------------------------------------------------

import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

# Bind and listen
server_socket.bind((host, port))
server_socket.listen(1)
print(f"✅ Server started on {host}:{port}")
print("Waiting for client connection...")

# Accept connection
conn, addr = server_socket.accept()
print(f"🔗 Connected to client: {addr}")

# Chat loop
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"\n📩 Client: {data}")

    if data.lower() == 'exit':
        print("❌ Client ended the chat.")
        break

    msg = input("You (Server): ")
    conn.send(msg.encode())

    if msg.lower() == 'exit':
        print("❌ Connection closed by server.")
        break

# Close connection
conn.close()
server_socket.close()
print("🔒 Server shutdown successfully.")
