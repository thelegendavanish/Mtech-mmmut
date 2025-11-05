# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Socket Programming for Echo / Ping / Talk Commands - Server
# Description:
#   This program implements a TCP server that can handle three modes:
#     1. Echo Mode  - Sends back received messages.
#     2. Ping Mode  - Responds to ping messages with latency info.
#     3. Talk Mode  - Enables two-way communication (chat) with the client.
# ------------------------------------------------------------------------------

import socket
import time

def start_server():
    host = socket.gethostname()
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"✅ Server started on {host}:{port}")
    print("Waiting for client connection...")
    conn, addr = server_socket.accept()
    print(f"🔗 Connected to client: {addr}")

    mode = conn.recv(1024).decode()
    print(f"\n🔧 Selected Mode: {mode}")

    if mode.lower() == "echo":
        echo_mode(conn)
    elif mode.lower() == "ping":
        ping_mode(conn)
    elif mode.lower() == "talk":
        talk_mode(conn)

    conn.close()
    server_socket.close()
    print("🔒 Server shutdown successfully.")


def echo_mode(conn):
    print("\n🪞 Echo Mode Activated.")
    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == "exit":
            print("❌ Echo session ended.")
            break
        print(f"📩 Received: {data}")
        conn.send(data.encode())


def ping_mode(conn):
    print("\n📡 Ping Mode Activated.")
    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == "exit":
            print("❌ Ping session ended.")
            break
        print("📩 Ping received, sending Pong...")
        conn.send("Pong".encode())


def talk_mode(conn):
    print("\n💬 Talk Mode Activated (Type 'exit' to end chat).")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"\nClient: {data}")
        if data.lower() == "exit":
            print("❌ Client ended chat.")
            break
        msg = input("You (Server): ")
        conn.send(msg.encode())
        if msg.lower() == "exit":
            print("❌ Chat ended by server.")
            break


if __name__ == "__main__":
    start_server()
