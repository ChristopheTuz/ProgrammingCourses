'''

	TITULO: Lectura y escritura en documentos csv
	FECHA: 030721
	AUTOR: Everest
	DESCRIPCIÓN: 
		Ejercicio sobre documentos csv. Poder abrir, leer y hacer unas pequeñas
			consultas con la información del archivo ./csv_data/Autos.csv
			La información debe de estar dentro de una carpeta llamada csv_data.
			O modificar el código en la función getNameDocument():

		NOTA: Los titulos no se toman en cuenta para el documento csv. Son manejados
			internamente.

DATA: Autos.csv

"ID","vehiculo","Millas por galon","cilindros","Potencia(HP)","Peso(1000lbs)","Cuarto de millas(s)"

"1","Mazda RX4",21,6,110,2.62,16.46
"2","Mazda RX4 Wag",21,6,110,2.875,17.02
"3","Datsun 710",22.8,4,93,2.32,18.61
"4","Hornet 4 Drive",21.4,6,110,3.215,19.44
"5","Hornet Sportabout",18.7,8,175,3.44,17.02
"6","Valiant",18.1,6,105,3.46,20.22
"7","Duster 360",14.3,8,245,3.57,15.84
"8","Merc 240D",24.4,4,62,3.19,20
"9","Merc 230",22.8,4,95,3.15,22.9
"10","Merc 280",19.2,6,123,3.44,18.3
"11","Merc 280C",17.8,6,123,3.44,18.9
"12","Merc 450SE",16.4,8,180,4.07,17.4
"13","Merc 450SL",17.3,8,180,3.73,17.6
"14","Merc 450SLC",15.2,8,180,3.78,18
"15","Cadillac Fleetwood",10.4,8,205,5.25,17.98
"16","Lincoln Continental",10.4,8,215,5.424,17.82
"17","Chrysler Imperial",14.7,8,230,5.345,17.42
"18","Fiat 128",32.4,4,66,2.2,19.47
"19","Honda Civic",30.4,4,52,1.615,18.52
"20","Toyota Corolla",33.9,4,65,1.835,19.9
"21","Toyota Corona",21.5,4,97,2.465,20.01
"22","Dodge Challenger",15.5,8,150,3.52,16.87
"23","AMC Javelin",15.2,8,150,3.435,17.3
"24","Camaro Z28",13.3,8,245,3.84,15.41
"25","Pontiac Firebird",19.2,8,175,3.845,17.05
"26","Fiat X1-9",27.3,4,66,1.935,18.9
"27","Porsche 914-2",26,4,91,2.14,16.7
"28","Lotus Europa",30.4,4,113,1.513,16.9
"29","Ford Pantera L",15.8,8,264,3.17,14.5
"30","Ferrari Dino",19.7,6,175,2.77,15.5
"31","Maserati Bora",15,8,335,3.57,14.6
"32","Volvo 142E",21.4,4,109,2.78,18.6


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

def getNameDocument():
 tempName = input("\n Give me a document name: ")
 if(tempName.upper() != "EXIT"): documentName = "./csv_data/" + tempName + ".csv"
 else:
  documentName = "EXIT"
  return documentName
 return documentName

def getCarModel():
 carModel = input("\n Give me a car model to search: ")
 return carModel

def getLbsLimits(documentName):
 li_lbs = input("\n Give me a botton limit to search: ")
 ls_lbs = input("\n Give me a top limit to search: ")
 searchCarByLbs(documentName,li_lbs,ls_lbs)
 return

def readDoc(documentName):
 file = open(documentName)
 csv_file = csv.reader(file)
 return csv_file

def printData(documentName):
 csvDocument = readDoc(documentName)
 print("\n")
 for line in csvDocument:
  print("",line)
 return

def searchCarByModel(documentName,model):
 csvDocument = readDoc(documentName)
 flag = False
 print("\n\t\tID, vehiculo, Millas por galon, cilindros, Potencia(HP), Peso(1000lbs), Cuarto de millas(s)")
 for line in csvDocument:
  carModel = line[1]
  if(carModel == model):
   print("\n Data found ->",line)
   flag = True
 if(flag==False): print("\n Data not found")
 return

def searchCarByLbs(documentName,li_lbs,ls_lbs):
 csvDocument = readDoc(documentName)
 bottonLimit = float(li_lbs)
 topLimit = float(ls_lbs)
 for line in csvDocument:
  data = float(line[5])
  if(data >= bottonLimit and data <= topLimit): print("\n ",line[0]," ",line[1],"\t\t\t",line[5],"lbs")
 return

def someQueries(documentName):
 flag = True
 while(flag==True):
  try:
   print("\n========================= Some queries ==========================\n")
   opc = int(input(" 1. Print data\n 2. Search car by model\n 3. Search car by weight (1000lbs)\n 4. Back\n\n Option: "))
   if(opc==1): printData(documentName)
   elif(opc==2):
   	carModel = getCarModel()
   	searchCarByModel(documentName,carModel)
   elif(opc==3): getLbsLimits(documentName)
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