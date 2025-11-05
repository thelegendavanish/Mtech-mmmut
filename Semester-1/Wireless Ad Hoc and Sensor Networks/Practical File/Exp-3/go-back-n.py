# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Implementation of Go-Back-N ARQ Protocol
# Description:
#   This program simulates the Go-Back-N (GBN) protocol used in reliable data
#   communication. In GBN, multiple frames are sent at once (as per window size),
#   but if any frame is lost, all subsequent frames are retransmitted.
# ------------------------------------------------------------------------------

import time
import random

def go_back_n():
    total_frames = int(input("Enter total number of frames: "))
    window_size = int(input("Enter window size: "))
    print("\n--- Go-Back-N ARQ Protocol Simulation ---\n")

    next_frame_to_send = 1

    while next_frame_to_send <= total_frames:
        # Send frames in the current window
        end_frame = min(next_frame_to_send + window_size - 1, total_frames)
        print(f"Sending frames {next_frame_to_send} to {end_frame}...")
        time.sleep(1)

        # Randomly simulate frame loss
        lost_frame = random.choice(range(next_frame_to_send, end_frame + 1))

        print(f"Frame {lost_frame} lost! Retransmitting from frame {lost_frame}...")
        next_frame_to_send = lost_frame
        time.sleep(1)

        # Assume retransmission is successful
        print(f"Frames {lost_frame} to {end_frame} retransmitted successfully.\n")
        next_frame_to_send = end_frame + 1

    print("All frames transmitted successfully.\n")

# Run program
go_back_n()
