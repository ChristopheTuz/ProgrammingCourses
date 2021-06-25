'''

	TITULO: base64_Decode_Encode
	FECHA: 240621
	AUTOR: Everest
	DESCRIPCIÓN: lower to up an up to lower (string)
		- token 64 (swap): uxvLihjVBgXVignVBIbLBcbWB2XSBW==
		- token 64 (no swap): UXVlIHJvbGxvIGNvbiBlbCBwb2xsbw==
		- token 32 (swap): kf2wkidsn5wgy3zamnxw4idfnqqha33mnrxq====
 		- token 32 (no swap): KF2WKIDSN5WGY3ZAMNXW4IDFNQQHA33MNRXQ====
		- Es necesario un token, lo primero que se tiene que hacer es hacer elegir
			si deseea swap a todas la letras, cambiando e mayuscula a minuscula y
			viciversa o usar el token real.Posteriormente se le aplica un decodebase64
			o un decodebase32 para obtemer la flag.

'''

import base64

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

def error():
 print("\n ERROR: Opción no valida")
 
'DECODE'
def reverse(tokenText,flag):
 if flag == 1:
  return tokenText.swapcase()
 return tokenText

def token64Toflag(tokenReverse):
 return base64.b64decode(tokenReverse)

def token32Toflag(tokenReverse):
 return base64.b32decode(tokenReverse)

def getToken():
 tokenText = input("\nGive me a token: " )
 return tokenText

def mainInitDecode(opc, status):
 token = getToken()
 tokenReverse = reverse(token, opc)
 if status == True:
  flag = token64Toflag(tokenReverse)
 else:
  flag = token32Toflag(tokenReverse)
 print("\nCorrect token:",tokenReverse)
 print("\nFlag:",flag)

def configResult64(opc, status):
 print("\nToken 64 (swapcase): uxvLihjVBgXVignVBIbLBcbWB2XSBW==")
 print("Token 64 (no swapcase): UXVlIHJvbGxvIGNvbiBlbCBwb2xsbw==")
 mainInitDecode(opc, status)
 
def configResult32(opc, status):
 print("\nToken 32 (swapcase): kf2wkidsn5wgy3zamnxw4idfnqqha33mnrxq====")
 print("Token 32 (no swapcase): KF2WKIDSN5WGY3ZAMNXW4IDFNQQHA33MNRXQ====")
 mainInitDecode(opc, status)
 
def funcMenu(w):
 flag = True
 while(flag==True):
  try:
      print("\n=================================================================")
      print("\n 1. Swapcase\n 2. No Swapcase\n 3. Atras")
      opc = int(input("\nOpcion deseada: "))
      if opc == 1:
       if w == 1:
        configResult64(opc, True)
       elif w == 2:
       	configResult32(opc, False)
      elif opc == 2:
       if w == 1:
       	configResult64(opc, True)
       elif w == 2:
       	configResult32(opc, False)
      elif opc == 3:
       flag = False
      else:
       error()
  except:
      error()

def mainDecode():
 flag = True
 while(flag==True):
  try:
      print("\n========================== DECODE FROM ==========================")
      print("\n 1. Base64\n 2. Base32\n 3. Atras")
      opc = int(input("\nOpcion deseada: "))
      if opc == 1 or opc == 2:
       funcMenu(opc)
      elif opc == 3:
       flag = False
      else:
       error()
  except:
      error()

'ENCODE'

def flag64Totoken(message):
 return base64.b64encode(message.encode()).decode()

def flag32Totoken(message):
 return base64.b32encode(message.encode()).decode()

def getFlag():
 flagText = input("\nGive me a message: " )
 return flagText

def mainInitEncode(status):
 message = getFlag()
 if status == True:
  token = flag64Totoken(message)
  print("\nToken 64:",token)
 else:
  token = flag32Totoken(message)
  print("\nToken 32:",token)

def mainEncode():
 flag = True
 while(flag==True):
  try:
      print("\n========================== ENCODE TO ==============================")
      print("\n 1. Base64\n 2. Base32\n 3. Atras")
      opc = int(input("\nOpcion deseada: "))
      if opc == 1:
      	mainInitEncode(True)
      elif opc == 2:
      	mainInitEncode(False)
      elif opc == 3:
       flag = False
      else:
       error()
  except:
      error()

'MAIN'
def mainMenu():
 flag = True
 while(flag==True):
  try:
      print("\n============================= MENU ==============================")
      print("\n 1. Decode\n 2. Encode\n 3. Salir")
      opc = int(input("\nOpcion deseada: "))
      if opc == 1:
      	mainDecode()
      elif opc == 2:
      	mainEncode()
      elif opc == 3:
       flag = False
      else:
       error()
  except:
      error()
      
if __name__ == "__main__":
 byEverest()
 mainMenu()