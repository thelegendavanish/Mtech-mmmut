# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Implementation of High-Level Data Link Control (HDLC)
# Description:
#   This program simulates the HDLC framing process using CRC for error detection.
#   It constructs HDLC frames, transmits them, and verifies data integrity.
# ------------------------------------------------------------------------------

# Function to compute CRC (Cyclic Redundancy Check)
def compute_crc(data, divisor="1001"):
    data = list(data)
    divisor = list(divisor)
    pick = len(divisor)
    tmp = data[:pick]

    while pick < len(data):
        if tmp[0] == '1':
            for i in range(len(divisor)):
                tmp[i] = str(int(tmp[i] != divisor[i]))
        tmp.pop(0)
        tmp.append(data[pick])
        pick += 1

    if tmp[0] == '1':
        for i in range(len(divisor)):
            tmp[i] = str(int(tmp[i] != divisor[i]))
    tmp.pop(0)
    return ''.join(tmp)


# Function to create an HDLC frame
def create_hdlc_frame(data):
    FLAG = "01111110"
    ADDRESS = "00000001"
    CONTROL = "00000011"

    divisor = "1001"
    crc = compute_crc(data + "000", divisor)
    data_with_crc = data + crc

    frame = FLAG + ADDRESS + CONTROL + data_with_crc + FLAG
    return frame, crc


# Function to simulate HDLC transmission
def simulate_hdlc():
    print("\n--- HDLC Protocol Simulation ---\n")
    data = input("Enter binary data to be transmitted: ")

    frame, crc = create_hdlc_frame(data)
    print("\nGenerated HDLC Frame:")
    print(frame)
    print("\nCRC (Error Checking Bits):", crc)

    # Receiver side simulation
    received = input("\nEnter received frame (or press Enter to use same frame): ")
    if not received:
        received = frame  # Use same frame if user presses Enter

    divisor = "1001"
    # Remove FLAG (8 bits), ADDRESS (8 bits), CONTROL (8 bits), FLAG (8 bits)
    data_with_crc = received[24:-8]

    remainder = compute_crc(data_with_crc, divisor)

    if set(remainder) == {'0'}:
        print("\n✅ Frame received correctly. No error detected.")
    else:
        print("\n❌ Error detected in received frame!")


# Run simulation
simulate_hdlc()



