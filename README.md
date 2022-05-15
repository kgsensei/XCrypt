# XCrypt

## About

This was initially a project to prove that I could make a strong encryption but I decided to publish it so that the internet people could improve it and use it. While it is still kinda basic it will get stronger and more efficient hopefully.

## To Use

To install XCrypt use the following command `pip install xcrypt` or `python -m pip install xcrypt`. After you install it be sure to import it with:

```py
import xcrypt
```

Now you can start to actually use XCrypt. XCrypt is a key file based encryption, so the first step in using it is to obtain a key. You can have someone else give you a key or you can generate one yourself. If you want to generate a key you can use the `xcrypt.make_key()` function. The return value of this function is equal to the key name (as a string). You will need this to encrypt and decrypt information.

```py
import xcrypt

print("Generating key")

keyName = xcrypt.make_key()

print("Key Name is " + keyName)

```

Now that you have a key file generated, the next step is to encrypt some information, the encrypted information must be a string. If it isn't a string it should be automatically converted. If you want to encrypt information the function you would use is `xcrypt.encrypt(keyName, Data)`. This function takes the key name (required for correct encryption) and the data/message to encrypt.

```py
import xcrypt

keyName = xcrypt.make_key()

encryptedData = xcrypt.encrypt(keyName, "Hello World!")

print(encryptedData) # This should output to a bunch of random characters.
```

After you have some information encrypted you probably want to decrypt it. The only way to do that is through the `xcrypt.decrypt(keyName, Data)` function. It takes two variables, keyName (for the key file name, same as the encryption function) and data (the encrypted text seen in variable `encryptedData` previously).

```py
import xcrpyt

keyName = "<Your Key File Name>"

encryptedData = "<Data Returned From Encrypt Function>"

decryptedData = xcrypt.decrypt(keyName, encryptedData)

print(decryptedData) # If everything worked then this should be "Hello World!".
```

Alright, now that we know exactly how to do everything lets put it together into one new file and test it. Each line will be commented explaining its purpose.

```py
import xcrypt # Import xcrypt so we can use the functions.

keyName = xcrypt.make_key() # Generate a key file and save the name to a variable.

initialData = input("Message To Encrypt/Decrypt: ") # Allow a user imputed message.

encryptedData = xcrypt.encrypt(keyName, initialData) # Save encrypted message to variable.

decryptedData = xcrypt.decrypt(keyName, encryptedData) # Save decrypted message to variable.

print("Message: " + initialData) # Display the initial message submitted.

print("Encrypted: " + encryptedData) # Display the encrypted form of the message.

print("Decrypted: " + decryptedData) # Display the decrypted form of the message.
```

Your finished! You have made a program that uses xcrypt to encrypt and decrypt messages.

A more rough example of this so far be seen in the `example.py` file.

Lets say you want a list of all the generated key files generated in a specific directory till this point. You can run the `xcrypt.locate_keys(directory)` function, the directory variable being the directory that you want to search. It also will search all subdirectories from the specified directory. For example:

```
 -> A
   -> B
     -> C
       -> D.key
       -> E.key
     -> F
       -> G.key
       -> H.key
     -> I.key
```

If you search the directory C, then the files found would be 'D.key' and 'E.key'. If you search directory B though... 'C/D.key', 'C/E.key', 'F/G.key', 'F/H.key' and 'I.key' would be found. This function will return a list with the relative path of each file. If this doesn't make sense, that's ok. There really isn't a huge reason to use this function.

If there are a lot of key files and you need a fast way to remove them all (and all of the keys in subdirectories, as shown in the `locate_keys()` example) then you can use this helpful function. `xcrypt.clear_keys(directory)` is a great function when it comes to getting rid of keys. Simply pass in the directory (same as `locate_keys()`) and it will delete the key files from that directory (and subdirectory). Since this is pretty straight forward, there won't be an example for this.

*Quick Note: All of the functions should require `xcrypt.` infront of them, this was excluded from the last example paragraph to make it easier to read. Thanks for understanding.*

## If There Are Issues

The only library it requires is random and that comes with python.  
Make sure your using the right key file when encrypting and decrypting.  
Make sure that your python version is compatable with XCrypt.
Check that the function names are correct (they updated in 1.2.0).
Make sure that your key file isn't corrupted.
Make sure that the key file works with your current version of XCrypt.

If you would like to report and issue please do so by one of the following methods:
 - Making a GitHub issue.
 - Joining my Discord server [HERE](https://discord.gg/U5A3QWXZKZ).
 - Emailing me.

##### Copyright &copy; kgsensei 2022.
