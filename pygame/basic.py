import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# text
score = pygame.font.Font('pygame/font/Pixeltype.ttf', 50)
score_surf = score.render('My game', False, 'Black') #format ('kata yang ditampilkan', huruf mulus atau tidak, warna)
score_rect = score_surf.get_rect(center = (400, 50))

#background
bg_surface = pygame.image.load('pygame/graphics/Sky.png').convert()
surface2 = pygame.image.load('pygame/graphics/ground.png').convert()

# menampilkan siput
snail = pygame.image.load('pygame/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(midbottom = (600, 300))

# menampilkan player
player_surf = pygame.image.load('pygame/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION : # MOUSEDOWN untuk mouse diklik dan MOUSEUP saat mouse dilepaskan
        #     if player_rect.collidepoint(event.pos):
        #         print('nice')

       
    screen.blit(bg_surface, (0,0))
    screen.blit(surface2, (0,300))
    screen.blit(score_surf, score_rect)
    screen.blit(snail, snail_rect)
    snail_rect.x -= 3

    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(player_surf, player_rect)

    # collision
    cek = 0
    collision = snail_rect.colliderect(player_rect)
    # if snail_rect.colliderect(player_rect) and cek==0:
    #     print("nice")

    # mouse_pos = pygame.mouse.get_pos()
    # print(mouse_pos)
    # pygame.mouse.get_pressed()
       


    

    pygame.display.update()
    clock.tick(60)