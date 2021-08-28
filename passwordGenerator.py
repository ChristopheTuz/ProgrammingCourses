from random import randrange, choice
import time

def randomChar(flag):
	opc = randrange(3)
	if(opc % 2 != 0 or flag == 0): letter = randomLetter()
	else: letter = choice(["¡","!","?","¿","#","$","&"])
	return letter

def randomLetter():
	opc = randrange(10)
	letter = choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"])
	if(opc % 2 == 0): return letter.upper()
	else: return letter

def randomNumber():
	number = str(randrange(10))
	return number

def passwordGenerator(flag,passwordSize):
	password = ""
	while flag < passwordSize:
		opc = randrange(3)
		if(opc == 1): tempPassword = randomLetter()
		elif(opc == 2): tempPassword = randomChar(flag)
		else: tempPassword = randomNumber()
		password = password + tempPassword
		flag += 1
	return password

def setUp(flag,size):
	while flag <= size:
		password = passwordGenerator(0,25)
		print(" Password generated:",password)
		flag += 1

if __name__ == "__main__":
	setUp(1,10)


#     f$Y2$a9¡32$QS2Ui?$Ñg97$d0
#     f$Y2$a9¡32$QS2Ui?$Ñg97$d1