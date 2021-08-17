import random
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
