# Import xcrypt file [xcrypt.py]
import xcrypt

# Define the message to encrypt and decrypt.
message = input("Message: ")

# Build the key and return key file name.
key = xcrypt.make_key()

# Encrypt message and display it on screen.
encrypted = xcrypt.encrypt(key, message)
print("\nEncrypted:", encrypted)

# Decrypt message and display it on screen.
decrypted = xcrypt.decrypt(key, encrypted)
print("\nDecrypted:", decrypted)
