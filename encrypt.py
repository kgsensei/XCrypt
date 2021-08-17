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
