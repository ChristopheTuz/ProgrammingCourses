'''

	TITULO: SHA integrity example
	FECHA: 280621
	AUTOR: Everest
	DESCRIPCIÓN: 
	 Ejercicio sobre SHA1. La opción de send message genera un token,
	 	el cual es el SHA1 del texto analizado. Mientras que el validate
	 	message genera el SHA1 del texto deseado y pide un token, el cual
	 	debe coincidir con el que se genera.

'''

import os
import platform
import hashlib

def byEverest():
 print("               .,:llooooooc..........:ooooooolc;.                        ")
 print("              ,loddddddddo;.        .;odddddddddo:.                      ")
 print("             ,odxxxxxxxxxl.          .lxxxxxxxxxxd:.                     ")
 print("            .cxxxxxxxxxxd,.          .;xxxxxxxxxxxo.                     ")
 print("            .cxxxxxxdoc:,..............;:loxxxxxxxd'                     ")
 print("            .lxxxdc;'......................';cdxxxd;                     ")
 print("          ..,oxxxdl;'.. ................ ..',cdxxxd:'..                  ")
 print("        ..'';oxxxxxxxoc,.   .......    .,codxxxxxxdc'''..                ")
 print("      ..'''';oxxxxxxddc;.              ':coxxxxxxxdc'''''..              ")
 print("    ..'''''';oxxxdddol,.  ...,;:;;,..   .'cooddxxxdc'''''''..            ")
 print("   .'''''''';oxdoc;'..   .;dOOkkO0Okc.    ..,;coxxdc'''''''''.           ")
 print("  .''''''''';oxc.         .'oko:dOx:.          'lxdc''''''''''.          ")
 print(" .'''''''''';ll.            .,;;::'             'ldc'''''''''''..        ")
 print(".''''''''''';:'      ......................      ,l:''''''''''''.        ")
 print("......................................................By. Ev3rest        ")

def error(flag):
 if(flag==1): print("\n ERROR: Invalid option\n")
 else: print("\n ERROR: Unknown\n")
 return

def validateFlag(flag):
 if(flag==True): print("\n Integrity OK")
 elif(flag==False): print("\n WARNING: Integrity compromised")
 else: error(-1)
 return

def systemDetect():
 systemD = platform.system()
 return systemD

def clearScreen():
 systemD = systemDetect()
 if(systemD == "Windows"): os.system("cls")
 elif(systemD == "Linux"): os.system("clear")
 else: error(-1)
 return

def systemPause():
 systemD = systemDetect()
 if(systemD == "Windows"): os.system("pause")
 elif(systemD == "Linux"): return
 else: error(-1)
 return

def getNameDocument():
 plaintText = input("\n Give me a document name to validate the message: ")
 return plaintText

def getTokenToValidate():
 token = input("\n Give me a token to validate a message: ")
 return token

def encryptTextSHA(encryptionType):
 plaintText = getNameDocument()
 tempDir = './'+plaintText
 with open(tempDir,"r") as doc:
  for line in doc:
   textC = line.encode("utf-8")
   temp = hashlib.new(encryptionType, textC)
   encrypted = temp.hexdigest()
 return encrypted

def validateMessage(encrypted):
 token = getTokenToValidate()
 value = (encrypted == token)
 validateFlag(value)
 return

def typeValidate(flag):
 if(flag==True):
 	encrypted = encryptTextSHA("sha1")
 	validateMessage(encrypted)
 else: error(-1)
 return

def mainSHA():
 flag=True
 while(flag==True):
  try: 
   print("\n=================================================================\n")
   opc = int(input(" 1. Send message\n 2. Validate message\n 3. Back\n\n Option: "))
   if(opc==1):
   	token = encryptTextSHA("sha1")
   	print("\n Your token is:",token)
   elif(opc==2): typeValidate(True) 
   elif(opc==3): flag = False
   else: error(1)
  except: error(1)
 return

def run():
 flag = True
 while(flag==True):
  clearScreen()
  byEverest()
  try:
   print("\n============================= SHA1 ==============================\n")
   opc = int(input(" 1. SHA1\n 2. Exit\n\n Option: "))
   if(opc==1): mainSHA()
   elif(opc==2):
   	print("\n Thank you, c-ya!\n")
   	flag = False
   else: error(1)
  except: error(1)
  systemPause()
 return

if __name__ == "__main__":
 run()
 clearScreen()
 systemPause()