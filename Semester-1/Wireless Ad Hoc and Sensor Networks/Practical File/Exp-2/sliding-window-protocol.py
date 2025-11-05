# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Implementation of Sliding Window Protocol
# Description:
#   This program simulates the Sliding Window protocol where multiple frames
#   are sent before receiving ACKs. It demonstrates the concept of window size
#   and continuous transmission for efficient data transfer.
# ------------------------------------------------------------------------------

import time
import random

def sliding_window():
    total_frames = int(input("Enter total number of frames: "))
    window_size = int(input("Enter window size: "))
    print("\n--- Sliding Window Protocol Simulation ---\n")

    sent = 0
    while sent < total_frames:
        # Send frames equal to window size
        print(f"Sending frames {sent + 1} to {min(sent + window_size, total_frames)}...")
        time.sleep(1)
        
        # Simulate random ACK loss
        ack_received = random.choice([True, False])
        
        if ack_received:
            print(f"ACK received for frames {sent + 1} to {min(sent + window_size, total_frames)}.\n")
            sent += window_size
        else:
            print(f"ACK lost! Retransmitting same window...\n")
            time.sleep(1)
    
    print("All frames transmitted successfully.\n")

# Run program
sliding_window()
