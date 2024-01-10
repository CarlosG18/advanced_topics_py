import pygame
from game import Game

#setup 
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

img_fundo = pygame.image.load("assets/cenarios/cenario.jpeg").convert_alpha()
img_fundo = pygame.transform.scale(img_fundo,(1280,720))

game = Game()

#loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.move_nave_principal(pygame.key.get_pressed())

    screen.blit(img_fundo,(0,0))
    game.upgrade(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()