import decode
import encode
import generate

message=input("Message: ")
key=generate.makeKey()
encrypted=encode.encode(key,message)
decrypted=decode.decode(key,encrypted)

print("Encrypted: "+encrypted)
print("Decrypted: "+decrypted)
