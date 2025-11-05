# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Hamming Code Generation, Error Detection & Correction
# Description: 
#   This Python program implements the Hamming Code technique for 
#   error detection and correction in digital communication systems.
#   The user provides binary data input, and the program:
#       1. Generates the encoded Hamming code with parity bits.
#       2. Accepts received data to check for transmission errors.
#       3. Displays the position of any detected error.
#       4. Provides an option to correct the erroneous bit automatically.
# ------------------------------------------------------------------------------


def calcRedundantBits(m):
    for i in range(m):
        if (2**i >= m + i + 1):
            return i


def posRedundantBits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''
    for i in range(1, m + r + 1):
        if (i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1
    return res[::-1]


def calcParityBits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if (j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        arr = arr[:n - (2**i)] + str(val) + arr[n - (2**i) + 1:]
    return arr


def detectError(arr, nr):
    n = len(arr)
    res = 0
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if (j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        res = res + val * (10**i)
    return int(str(res), 2)


def correctError(arr, error_pos):
    n = len(arr)
    arr = list(arr)
    pos = n - error_pos  # convert from right-based position to left-based index
    arr[pos] = '1' if arr[pos] == '0' else '0'
    return ''.join(arr)


# --- MAIN PROGRAM ---

print("=== Hamming Code Generation, Error Detection & Correction ===\n")

# Step 1: Input data
data = input("Enter the binary data to be transmitted: ").strip()

# Step 2: Encode data with redundant bits
m = len(data)
r = calcRedundantBits(m)
arr = posRedundantBits(data, r)
arr = calcParityBits(arr, r)

print("\nData transferred is:", arr)

# Step 3: Input received data
received = input("\nEnter the received data (with or without error): ").strip()

# Step 4: Detect error
correction = detectError(received, r)
if correction == 0:
    print("\n✅ No error detected in received data.  ")
else:
    print(f"\n⚠️ Error detected at bit position {len(received) - correction + 1} from the left.")

    # Step 5: Ask user if they want to correct the error
    choice = input("\nDo you want to correct the error? (y/n): ").strip().lower()
    if choice == 'y':
        corrected = correctError(received, correction)
        print("\n✅ Corrected data is:", corrected)
    else:
        print("\nNo correction performed.")
