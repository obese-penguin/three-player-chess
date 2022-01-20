import pygame
import numpy as np

with open('coords.txt') as file:
    a = file.readline()
b = []
for i in a.split('], '):
    j = i
    j += ']'
    b.append(j)

pygame.init()
white = (255, 255, 255)

X = 800
Y = 800

display_surface = pygame.display.set_mode((X, Y ))

pygame.display.set_caption('Image')
path = 'resized2-chessimg.jpeg'

image = pygame.image.load(path)

while True :

    display_surface.fill(white)
    display_surface.blit(image, (0, 0))
    x, y = pygame.mouse.get_pos()
    r = round(np.sqrt((x-400)**2 + (y-400)**2),2)
    ang = round(np.arctan2(y-400, x-400),2)
    d = int(abs((r-96))//50)
    coordangle = int((ang*57.2)//15)
    if coordangle<0:
        coordangle = 24+coordangle

    print(coordangle,d,x,y)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        pygame.display.update()
