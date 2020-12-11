import pygame
pygame.init()

window = pygame.display.set_mode((600,600)) #urgun undur
isRunning = True

xImg = pygame.image.load("x.png")
oImg = pygame.image.load("o.png")

while isRunning:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False

	window.fill((255,255,255))
	window.blit(oImg,(0,0)) #zurag, x, y
	pygame.display.update()
