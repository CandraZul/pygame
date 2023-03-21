import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('pygame/font/Pixeltype.ttf', 50)


bg_surface = pygame.image.load('pygame/graphics/Sky.png').convert()
surface2 = pygame.image.load('pygame/graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black') #format ('kata yang ditampilkan', huruf mulus atau tidak, warna)

snail = pygame.image.load('pygame/graphics/snail/snail1.png').convert_alpha()
snail_x_position = 600
snail_rect = snail.get_rect(midbottom = (snail_x_position, 300))

player_surf = pygame.image.load('pygame/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
       
    screen.blit(bg_surface, (0,0))
    screen.blit(surface2, (0,300))
    screen.blit(text_surface, (350, 50))
    screen.blit(snail, snail_rect)
    snail_rect.left -= 3

    if snail_rect.left <= -50:
        snail_rect.left = 800

    screen.blit(player_surf, player_rect)

    

    pygame.display.update()
    clock.tick(60)