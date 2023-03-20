import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

bg_surface = pygame.image.load('pygame/graphics/Sky.png')
surface2 = pygame.image.load('pygame/graphics/ground.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
       
        screen.blit(bg_surface, (0,0))
        screen.blit(surface2, (0,300))
        
        

        pygame.display.update()
        clock.tick(60)