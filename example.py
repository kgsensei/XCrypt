# Import xcrypt file [./xcrypt.py]-
# used for generating a valid key file.
import xcrypt

# Define the message to encrypt and decrypt.
message = input("Message: ")

# Make newline before printing encrypted-
# and decrypted data. It looks better.
print("")

# Build the key and return key file name.
key = xcrypt.makeKey()

# Encrypt data, pass in the key and message-
# to encrypt. Return the encryted message.
encrypted = xcrypt.encode(key, message)

# Decrypt data, pass in key and encrypted-
# message to decrypt. Return plain text message.
decrypted = xcrypt.decode(key, encrypted)

# Print encrypted message, str by default
print("Encrypted: " + encrypted)

# Make newline in between printing encrypted-
# and decrypted data. It looks better.
print("")

# Print decrypted message, str by default.
print("Decrypted: " + decrypted)
