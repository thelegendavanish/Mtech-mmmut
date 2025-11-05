# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Implementation of Selective Repeat ARQ Protocol
# Description:
#   This program simulates the Selective Repeat (SR) protocol used in reliable
#   data communication. In SR, only the specific frames that are lost are
#   retransmitted, rather than the entire window, improving efficiency.
# ------------------------------------------------------------------------------

import time
import random

def selective_repeat():
    total_frames = int(input("Enter total number of frames: "))
    window_size = int(input("Enter window size: "))
    print("\n--- Selective Repeat ARQ Protocol Simulation ---\n")

    sent = 0
    while sent < total_frames:
        end_frame = min(sent + window_size, total_frames)
        print(f"Sending frames {sent + 1} to {end_frame}...")
        time.sleep(1)

        # Randomly select some frames that are lost
        lost_frames = random.sample(range(sent + 1, end_frame + 1), k=random.randint(0, 2))

        if lost_frames:
            print(f"Frames lost: {lost_frames}")
            time.sleep(1)
            print(f"Retransmitting lost frames {lost_frames}...\n")
        else:
            print("All frames received successfully.\n")

        sent = end_frame

    print("All frames transmitted successfully.\n")

# Run program
selective_repeat()
