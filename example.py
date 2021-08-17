#Import decrypt file [./decrypt.py]-
#used for decrypting the encrypted data.
import decrypt

#Import encrypt file [./encrypt.py]-
#used for encrypting plain text message.
import encrypt

#Import generate file [./generate.py]-
#used for generating a valid key file.
import generate

#Define the message to encrypt and decrypt.
message=input("Message: ")

#Build the key and return key file name.
key=generate.makeKey()

#Encrypt data, pass in the key and message-
#to encrypt. Return the encryted message.
encrypted=encrypt.encode(key,message)

#Decrypt data, pass in key and encrypted-
#message to decrypt. Return plain text message.
decrypted=decrypt.decode(key,encrypted)

#Print encrypted message, str by default
print("Encrypted: "+encrypted)

#Print decrypted message, str by default.
print("Decrypted: "+decrypted)
