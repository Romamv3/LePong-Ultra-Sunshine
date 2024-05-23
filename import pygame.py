import pygame

pygame.init()

screen = pygame.display.setmode((800, 600)) 
camera = pygame.Surface((800, 600))

#Create a circle shape
pygame.draw circle(camera, (255, 0, 0), (50, 50), 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT

:        

            running = False
    screen.blit(camera, (0, 0))
    pygame.display.flip()