"""
A lightweight encryption library in python.
By: kgsensei, with help from: DKellem & Sigmanificient
"""

import random
import os

FUNCTIONAL_CHARACTERS="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./;<=>@[\\]^_`{|}~"

def read_key(key_path):
	"""
	Return a pre-parsed of the given key path.
	:param key_path:str
		Path to the key file.
	:return List[Tuple[str,str]]
		Pre-parsed key file.
	"""
	if os.path.exists(key_path):
		with open(key_path)as file:key_file=file.readlines()[1:-1]
		key_file_contents=[(line[4:].replace("\n",""),line[0])for line in key_file]
		return key_file_contents[1::]
	else:
		raise FileNotFoundError("Key file couldn't be found.")

def encrypt(key_path,message):
	"""
	Encrypt data.
	:param key_path:str
		Path to the key file.
	:param message:str
		Data/Message to encrypted.
	:return str
		Ciphered message.
	"""
	key_file_contents=read_key(key_path)
	return_message=""
	message=str(message)
	for letter in message.strip():
		if letter==" ":
			return_message+=":"
		for code in key_file_contents:
			if code[1]==letter:
				enc=code[0].split("?")
				return_message+=enc[random.randint(0,7)]
		return_message+="?"
	return return_message[:-1]

def decrypt(key_path,message):
	"""
	Decrypt data.
	:param key_path:str
		Path to the key file.
	:param message:str
		Encrypted-Data/Message to decrypt.
	:return str
		Plain text data/message.
	"""
	key_file_contents=read_key(key_path)
	return_message:str=""
	message=str(message)
	for code in message.split("?"):
		if code==":":return_message+=" "
		for (code_enc,code_letter)in key_file_contents:
			if code in code_enc.split("?"):
				return_message+=code_letter
	return return_message

def generate25():
	"""Generates a sequence of random characters between 15 and 20 characters."""
	return ''.join(random.choice(FUNCTIONAL_CHARACTERS)for _ in range(random.randint(15,20)))

def generate4():
	"""Generates a sequence of 4 random characters."""
	return ''.join(random.choice(FUNCTIONAL_CHARACTERS)for _ in range(4))

def make_key():
	"""
	Build the key and return key file name.
	:return str
		The filename of the generated xcrypt key.
	"""
	generation_base=random.randint(1000,9999)
	file_key=["xcrypt-key".center(160),(f"{generation_base}4kezuihg8i4wz"+'?'.join(generate25()for _ in range(7)))]
	file_key.extend((f"{character}{generate4()}{generate25()}?"+'?'.join(generate25()for _ in range(7)))for character in FUNCTIONAL_CHARACTERS)
	file_key.append("xcrypt-key".center(160))
	with open(f"{generation_base}_xcrypt.key","w+")as f:f.write('\n'.join(file_key))
	return f"{generation_base}_xcrypt.key"

def locate_keys(directory):
	"""
	Search directory and return key files found.
	:param directory:str
		The directory to search for key files in.
	:return list
		A list of key file names located in directory.
	"""
	if os.path.exists(directory):
		keyFileList=[]
		for root,dirs,files in os.walk(directory):
			for file in files:
				if(file.endswith("_xcrypt.key")):
					keyFileList.append(os.path.join(root,file))
		return keyFileList
	else:
		raise NotADirectoryError("Directory does not exist.")

def clear_keys(directory):
	"""
	Search directory and delete key files found.
	:param directory:str
		The directory to search for key files in.
	:return bool
		True if it deleted found key files.
	"""
	if os.path.exists(directory):
		for root,dirs,files in os.walk(directory):
			for file in files:
				if(file.endswith("_xcrypt.key")):
					os.remove(os.path.join(root,file))
		return True
	else:
		raise NotADirectoryError("Directory does not exist.")
