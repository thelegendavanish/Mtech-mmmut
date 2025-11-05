# ------------------------------------------------------------------------------
# Author: Avanish Kumar
# Title: Implementation of Data Encryption and Decryption
# Description:
#   This program demonstrates a simple example of symmetric encryption
#   and decryption using a Caesar Cipher technique.
#   The user enters plain text and a key value, and the program
#   encrypts and decrypts the message accordingly.
# ------------------------------------------------------------------------------

def encrypt(text, key):
    """Encrypts text using Caesar Cipher."""
    encrypted = ""
    for char in text:
        if char.isupper():
            encrypted += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            encrypted += chr((ord(char) + key - 97) % 26 + 97)
        else:
            encrypted += char
    return encrypted


def decrypt(cipher, key):
    """Decrypts text using Caesar Cipher."""
    decrypted = ""
    for char in cipher:
        if char.isupper():
            decrypted += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            decrypted += chr((ord(char) - key - 97) % 26 + 97)
        else:
            decrypted += char
    return decrypted


def main():
    print("\n=== Data Encryption and Decryption using Caesar Cipher ===\n")
    
    plaintext = input("Enter the message to encrypt: ")
    key = int(input("Enter the key (1-25): "))

    cipher = encrypt(plaintext, key)
    print(f"\n🔐 Encrypted Message: {cipher}")

    choice = input("\nDo you want to decrypt it? (y/n): ").lower()
    if choice == 'y':
        decrypted = decrypt(cipher, key)
        print(f"\n🔓 Decrypted Message: {decrypted}")
    else:
        print("\nExiting without decryption.")


if __name__ == "__main__":
    main()





