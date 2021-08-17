# Import xcrypt file [./xcrypt.py]-
# used for generating a valid key file.
import xcrypt

# Define the message to encrypt and decrypt.
message = input("Message: ")

# Build the key and return key file name.
key = xcrypt.make_key()

encrypted: str = xcrypt.encode(key, message)
print("\nEncrypted:", encrypted)


decrypted: str = xcrypt.decode(key, encrypted)
print("\nDecrypted:", decrypted)
