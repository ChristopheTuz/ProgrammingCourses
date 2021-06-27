import os
import platform

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
 if(flag==1):
  print("\n ERROR: Invalid option\n")
 elif(flag==2):
  print("\n ERROR: Key 1 to 25\n")
 else:
  print("\n ERROR: Unknown\n")
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

def getKey():
 key = int(input(" Key: "))
 if(key>=1 and key<=25): return key
 else:
  error(2)
  return -1
 return

def getText():
 plainText = input(" Give a mesagge: ")
 return plainText

def encodeCesar(text,key):
 ascUP = 65
 ascLOW = 97
 alph = 26
 if(text == ' '): return text
 else:
  if(text.isupper()):
   x = ((ord(text) + key - ascUP) % alph)
   temp = x + ascUP
  else:
   x = ((ord(text) + key - ascLOW) % alph)
   temp = x + ascLOW
  ncd = chr(temp)
  return ncd

def decodeCesar(text, key):
 ascUP = 65
 ascLOW = 97
 alph = 26
 if(text == ' '): return text
 else:
  if(text.isupper()):
   x = ((ord(text) - key - ascUP) % alph)
   temp = x + ascUP
  else:
   x = ((ord(text) - key - ascLOW) % alph)
   temp = x + ascLOW
  dcd = chr(temp)
  return dcd

def encodeSet():
 print("\n============================ ENCODE =============================\n")
 keyToken = getKey()
 if(keyToken!=-1):
  capText = getText()
  ncd = ''
  for c in capText: ncd += encodeCesar(c,keyToken)
  print(" Encode mesagge: "+ncd+" ["+str(keyToken)+"]\n")
 return

def decodeSet():
 print("\n============================ DECODE =============================\n")
 keyToken = getKey()
 if(keyToken!=-1):
  capText = getText()
  dcd = ''
  for c in capText: dcd += decodeCesar(c,keyToken)
  print(" Decode mesagge: "+dcd+"\n")
 return
 
def run():
 flag = True
 while(flag==True):
  clearScreen()
  byEverest()
  try:
   print("\n============================= ROTn ==============================\n")
   opc = int(input(" 1. Encode\n 2. Decode\n 3. Exit\n\n Option: "))
   if(opc==1): encodeSet()
   elif(opc==2): decodeSet()
   elif(opc==3): 
   	print("\n Thank you, c-ya!\n")
   	flag = False
   else: error(1)
  except: error(1)
  systemPause()
 return

if __name__ == "__main__":
 run()
 clearScreen()