import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('pygame/font/Pixeltype.ttf', 50)

bg_surface = pygame.image.load('pygame/graphics/Sky.png')
surface2 = pygame.image.load('pygame/graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black') #format ('kata yang ditampilkan', huruf mulus atau tidak, warna)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
       
        screen.blit(bg_surface, (0,0))
        screen.blit(surface2, (0,300))
        screen.blit(text_surface, (350, 50))
        

        pygame.display.update()
        clock.tick(60)