'''
La conjetura de Collatz, conocida también como conjetura 3n+1 o conjetura de Ulam (entre otros nombres), fue enunciada por el matemático Lothar Collatz en 1937, y a la fecha no se ha resuelto.
Sea la siguiente operación, aplicable a cualquier número entero positivo:
Si el número es par, se divide entre 2.
Si el número es impar, se multiplica por 3 y se suma 1.
'''

import matplotlib.pyplot as matpy

y = []
x = []

def getNumber():
	number = int(input("\n Type a number: "))
	return number

def collatz(number):
	steps = 0; x.append(0); y.append(number)
	while(number != 1):
		x.append(steps); steps += 1
		if(number == 1): y.append(1)
		elif(number % 2 == 0): number = number / 2; y.append(number)
		elif(number % 2 != 0): number = (number * 3) + 1; y.append(number)
	return steps

def run():
	number = getNumber()
	nSteps = collatz(number)
	print("\n\n Conjetura de Collatz\n")
	for element in y: print(int(element), end = " ")
	print("\n\n Steps:",nSteps)
	print("\n Max value:", max(y))
	matpy.figure('La conjetura de Collatz')
	#matpy.scatter(x, y);
	matpy.plot(x, y)
	matpy.xlabel("Steps"); matpy.ylabel("Collatz")
	matpy.show()

if __name__ == "__main__":
	run()