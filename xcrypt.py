import random

def encode(key_path:str,message:str):
     key_file=open(key_path).readlines()
     key_file_contents=[]
     key_file.pop(-1)
     key_file.pop(0)
     for line in key_file:key_file_contents.append((line[4:].replace("\n",""),line[0]))
     key_file_contents.pop(0)
     return_message=""
     if message[0]==" ":message=message[1:]
     if message[-1]==" ":message=message[:-1]
     for letter in message:
          if letter==" ":return_message=return_message+":"
          for code in key_file_contents:
               if code[1]==letter:
                    enc=code[0].split("?")
                    return_message=return_message+enc[random.randint(0,7)]
          return_message=return_message+"?"
     if return_message[-1]=="?":return_message=return_message[:-1]
     return return_message

def decode(key_path:str,message:str):
     key_file=open(key_path).readlines()
     key_file_contents=[]
     key_file.pop(-1)
     key_file.pop(0)
     for line in key_file:key_file_contents.append((line[4:].replace("\n",""),line[0]))
     key_file_contents.pop(0)
     return_message=""
     message=message.split("?")
     for code in message:
          if code==":":return_message=return_message+" "
          for item in key_file_contents:
               enc=item[0].split("?")
               if code in enc:return_message=return_message+item[1]
     return return_message

def generate25():
     return ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ2034567890!@#$%^&*()-=_+{}[];\'\",.<>/|") for x in range(random.randint(15,25)))

def generate4():
     return ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ2034567890!@#$%^&*()-=_+{}[];\'\",.<>/|") for x in range(0,3))

def makeKey():
     generation_base=random.randint(1000,9999)
     inu=70
     file_key=[]
     functional_characters="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./;<=>@[\\]^_`{|}~"
     generation_seed=[
          random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),
          random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9)
     ]
     file_key.append("-"*inu+"xcrypt-key"+"-"*inu)
     file_key.append(str(generation_base)+"4kezuihg8i4wz"+generate25()+"?"+generate25()+"?"+generate25()+"?"+generate25()+generate25()+"?"+generate25()+"?"+generate25())
     for character in functional_characters:
          file_key.append(character+generate4()+generate25()+"?"+generate25()+"?"+generate25()+"?"+generate25()+"?"+generate25()+"?"+generate25()+"?"+generate25()+"?"+generate25())
     file_key.append("-"*inu+"xcrypt-key"+"-"*inu)
     f=open(str(generation_base)+"_xcrypt.key","w+")
     for line in file_key:f.write(line+"\n")
     f.close()
     return str(generation_base)+"_xcrypt.key"
