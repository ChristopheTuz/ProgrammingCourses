'''

  TITULO: Lectura de documentos GFF como csv y escritura csv
  FECHA: 050721
  AUTOR: Everest
  DESCRIPCION: Lee un documento GFF (WIKIPEDIA: En bioinformática, el
    formato de características generales es un formato de archivo que
    se utiliza para describir genes y otras características de secuencias
    de ADN, ARN y proteínas.) Despues de leer los datos, se pide un 
    delimitador de tres caracteres que se encuentra al principio en cada
    una de las lineas de cada archivo (NC_ o NZ_ etc). Con el fin de poder
    discrimiar las lineas que no son necesarias. En el menú para hacer las
    consultas podemos imprimir en pantalla la información que contenga 
    la cadena "ID=gene", haciendo referencia a un gen. Al mismo tiempo se
    guarda en un documento llamado csv-data.csv toda la información filtrada.


    Principal referencia: https://ftp.ncbi.nlm.nih.gov
    Documento referencia: https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/006/945/GCF_000006945.2_ASM694v2/

'''

import os
import csv
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

def info(flag):
 if(flag==1): print("\n ERROR: Invalid option\n")
 elif(flag==2): print("\n ERROR: Load data first\n")
 elif(flag==3): print("\n ERROR: Already data loaded\n")
 elif(flag==400): print("\n Successfully: Data OK\n")
 elif(flag==401): print("\n Successfully: Session close\n")
 elif(flag==402): print("\n Successfully: Document created\n")
 elif(flag==777): print("\n Thank you, c-ya!\n")
 else: print("\n ERROR: Unknown\n")
 return

def systemDetect():
 systemD = platform.system()
 return systemD

def clearScreen():
 systemD = systemDetect()
 if(systemD == "Windows"): os.system("cls")
 elif(systemD == "Linux"): os.system("clear")
 else: info(-1)
 return

def systemPause():
 systemD = systemDetect()
 if(systemD == "Windows"): os.system("pause")
 elif(systemD == "Linux"): return
 else: info(-1)
 return

def getDelimiter():
 delimiter = input("\n Dalimiter [solo tres caracteres(Ejemplo: 'NZ_' )]: ")
 return delimiter

def getNameDocument():
 tempName = input("\n Give me a document name: ")
 if(tempName.upper() != "EXIT"): documentName = "./csv_data/" + tempName
 else:
  documentName = "EXIT"
  return documentName
 return documentName

def readDoc(documentName):
 file = open(documentName)
 csv_file = csv.reader(file, delimiter='\t')
 return csv_file

def writeDoc(data):
  with open('./data-csv.csv', 'a') as f:
    f.write(data)
  return

def printData(documentName):
 csvDocument = readDoc(documentName)
 delimiter = getDelimiter()
 print("\n")
 cant=0
 flag=0
 for line in csvDocument:
  tempInit = line[0]
  sInit = tempInit[0:3]
  if(sInit == delimiter):
   tempS = line[8]
   s = tempS[0:7]
   if(s == "ID=gene"):
    print(line)
    data = line[8] + "\n"
    writeDoc(data)
    flag+=1
  cant+=1
 info(402)
 print("Lineas leidas:",cant,"\t Lineas igual a 'ID=gene':",flag)
 return

def someQueries(documentName):
 flag = True
 while(flag==True):
  try:
   print("\n========================= Some queries ==========================\n")
   print("\n Documento actual: ",documentName,"\n")
   opc = int(input(" 1. Print data\n 4. Back\n\n Option: "))
   if(opc==1): printData(documentName)
   elif(opc==4): flag = False
   else: info(1)
  except: info(1)
 return

def run():
 flag=True
 queryFlag=False
 while(flag==True):
  clearScreen()
  byEverest()
  try:
   print("\n============================= CSV ===============================\n")
   opc=int(input(" 1. Load data\n 2. Some queries\n 3. Close session\n 4. Exit\n\n Option: "))
   if(opc==1):
    if(queryFlag==True):
     documentName = getNameDocument()
     info(400)
    elif(queryFlag==False):
     documentName = getNameDocument()
     queryFlag = True
     info(400)
    else: info(1)
   elif(opc==2):
    if(queryFlag==True):someQueries(documentName)
    else: info(2)
   elif(opc==3):
    queryFlag = False
    info(401)
   elif(opc==4):
    flag = False
    info(777)
   else: info(1)
  except:
    info(1)
  systemPause()
 return

if __name__ == '__main__':
 run()