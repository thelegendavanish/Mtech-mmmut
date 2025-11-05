# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Socket Programming for Echo / Ping / Talk Commands - Client
# Description:
#   This program connects to the server and supports three commands:
#     1. Echo  - Sends data and receives it back.
#     2. Ping  - Sends "ping" and measures round-trip time.
#     3. Talk  - Enables interactive chat between client and server.
# ------------------------------------------------------------------------------

import socket
import time

def start_client():
    host = socket.gethostname()
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"🔗 Connected to server {host}:{port}")

    print("\nAvailable Modes: echo / ping / talk")
    mode = input("Enter mode: ").lower()
    client_socket.send(mode.encode())

    if mode == "echo":
        echo_mode(client_socket)
    elif mode == "ping":
        ping_mode(client_socket)
    elif mode == "talk":
        talk_mode(client_socket)
    else:
        print("❌ Invalid mode selected.")

    client_socket.close()
    print("🔒 Client shutdown successfully.")


def echo_mode(client_socket):
    print("\n🪞 Echo Mode (type 'exit' to quit)")
    while True:
        msg = input("You: ")
        client_socket.send(msg.encode())
        if msg.lower() == "exit":
            break
        data = client_socket.recv(1024).decode()
        print(f"Server Echoed: {data}")


def ping_mode(client_socket):
    print("\n📡 Ping Mode (type 'exit' to quit)")
    while True:
        msg = input("Send ping? (y/n): ").lower()
        if msg == 'n':
            break
        start_time = time.time()
        client_socket.send("ping".encode())
        response = client_socket.recv(1024).decode()
        end_time = time.time()
        print(f"Response: {response} | Round Trip Time: {(end_time - start_time):.4f} sec")
    client_socket.send("exit".encode())


def talk_mode(client_socket):
    print("\n💬 Talk Mode (type 'exit' to quit)")
    while True:
        msg = input("You (Client): ")
        client_socket.send(msg.encode())
        if msg.lower() == "exit":
            break
        data = client_socket.recv(1024).decode()
        print(f"\nServer: {data}")
        if data.lower() == "exit":
            break


if __name__ == "__main__":
    start_client()
