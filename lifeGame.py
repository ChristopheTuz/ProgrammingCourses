import pygame
import numpy as np
import time

# Ancho y alto de la pantalla
width, height = 800,800

# Paleta de colores
background = 25, 25, 25 # Color del fondo de pantalla
LIVE_COLOR = (255,255,255) # Celula viva
DEAD_COLOR = (128,128,128) # Celula muerta

# Numero de columnas y filas (CELDAS)
columsX, rowsY = 80, 80

dimCelW = width / columsX
dimCelH = height / rowsY

# Inicializamos pygame
pygame.init()

# Creación de la pantalla
screen = pygame.display.set_mode((height, width))

# Matriz inicializada en ceros. 1 = Vivo, 0 = Muerto
gameState = np.zeros((columsX, rowsY))

# GameStatus
gamePause = False
gameRun = True

# Bucle de ejecución
while gameRun:

	newGameState = np.copy(gameState) # Copiar el status

	for event in pygame.event.get():
		if event.type == pygame.QUIT: gameRun = False
		if event.type == pygame.KEYDOWN: gamePause = not gamePause
		mouseClick = pygame.mouse.get_pressed()
		if sum(mouseClick) > 0:
			posX, posY = pygame.mouse.get_pos()
			x, y = int(np.floor(posX/dimCelH)), int(np.floor(posY/dimCelW))
			newGameState[x, y] = not mouseClick[2]

	screen.fill(background) # Limpiar el fondo de pantalla

	for y in range(0, columsX):
		for x in range(0, rowsY):

			if not gamePause:

				# Calcular la cantidad de vecinos adyacentes
				friends = gameState[(x - 1) % columsX, (y - 1) 	% rowsY] + gameState[(x) 	 % columsX, (y - 1) 	% rowsY] + \
						  gameState[(x + 1) % columsX, (y - 1) 	% rowsY] + gameState[(x - 1) % columsX, (y) 		% rowsY] + \
						  gameState[(x + 1) % columsX, (y)		% rowsY] + gameState[(x - 1) % columsX, (y + 1) 	% rowsY] + \
						  gameState[(x) 	% columsX, (y + 1) 	% rowsY] + gameState[(x + 1) % columsX, (y + 1) 	% rowsY]
						  
                # Rule 1: Si una célula está muerta y tiene tres vecinas vivas, nace.
				if gameState[x,y] == 0 and friends==3:
					newGameState[x,y] = 1

                # Rule 2: Si una celula viva con mas de 3 vecinos o menos de 2, muere.
				elif gameState[x,y] == 1 and (friends < 2 or friends > 3):
					newGameState[x,y] = 0

			# Coordenadas de los rectangulos definidos, se crea un poligono para cada celda a dibujar.
			poly = [((x)		*	dimCelW, y			*	dimCelH),
					((x + 1)	*	dimCelW, y 			*	dimCelH),
					((x + 1)	*	dimCelW, (y + 1)	*	dimCelH),
					((x)		*	dimCelW, (y + 1)	* 	dimCelH)]

			# Dibujar la celda para cada par de coordenadas x, y.
			if newGameState[x, y] == 1:
				pygame.draw.polygon(screen, LIVE_COLOR, poly, 0)
			else:
				pygame.draw.polygon(screen, DEAD_COLOR, poly, 1)

	# Actualización de los estados
	gameState = np.copy(newGameState)

	# Esperar 0.1 segundos
	time.sleep(0.1)

	# Actualización de la pantalla
	pygame.display.flip()

pygame.quit()