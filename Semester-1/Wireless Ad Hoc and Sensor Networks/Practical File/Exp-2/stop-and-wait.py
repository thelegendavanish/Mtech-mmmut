# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Implementation of Stop and Wait Protocol
# Description:
#   This program simulates the Stop and Wait protocol used in data communication.
#   The sender transmits one frame at a time and waits for an acknowledgment (ACK)
#   before sending the next frame. If ACK is lost, the frame is retransmitted.
# ------------------------------------------------------------------------------

import time
import random

def stop_and_wait():
    n = int(input("Enter number of frames to send: "))
    frames = list(range(1, n + 1))
    print("\n--- Stop and Wait Protocol Simulation ---\n")

    for frame in frames:
        print(f"Sending frame {frame}...")
        time.sleep(1)
        
        # Simulate random ACK loss
        ack = random.choice([True, False])
        
        if ack:
            print(f"ACK for frame {frame} received.\n")
        else:
            print(f"ACK for frame {frame} lost! Retransmitting frame {frame}...\n")
            time.sleep(1)
            print(f"Frame {frame} retransmitted successfully.\n")

    print("All frames transmitted successfully.\n")

# Run program
stop_and_wait()
