# Xcrypt
#### A lightweight encryption and decryption library for Python.

## How to use

Run `pip install xcrypt` to add xcrypt to your python libraries. After that you  
need you import it using `import xcrypt`, but you probably knew that already.

Once you have it imported you can start using xcrypt. First, you need a working  
key file. You can get this by using the `xcrypt.make_key()` script. Now that you  
have that you will need to use that key to encrypt something, like so:  
`xcrypt.encode(<key path>,<message>)` in this case that would be  
`xcrypt.encode('./my_xcrypt.key','Hello World!')`. This will return the encrypted  
text as a string, its roughly the same for the decrypt function.

Here is an example for generating a key, encrypting data using the key and  
decrypting the encrypted data, of course using the key.
```py
# Import xcrypt file [xcrypt.py]
import xcrypt

# Define the message to encrypt and decrypt.
message = input("Message: ")

# Build the key and return key file name.
key = xcrypt.make_key()

# Encrypt message and display it on screen.
encrypted = xcrypt.encode(key, message)
print("\nEncrypted:" + encrypted)

# Decrypt message and display it on screen.
decrypted = xcrypt.decode(key, encrypted)
print("\nDecrypted:" + decrypted)

# Input to prevent exit right away upon run.
input("")
```

## Dealing with issues

Make sure your using a python version compatible with xcrypt. (3.6+)  
Check to make sure the key file isn't broken or missing, also,  
make sure your using the same key file for encryption and decryption.

If your going to make a GitHub issue or report an issue in my discord server  
please make sure to include the following information.
- Python version your using
- XCrypt version your using
- PIP version your using
- Any XCrypt modifications you did
- Key file your using or a different key file you generated
- Code your using (optional)

#### XCrypt is copyright of kgsensei, 2021.