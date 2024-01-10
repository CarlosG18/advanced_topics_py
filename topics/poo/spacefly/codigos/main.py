import pygame
#from game import Game
from nave import Nave

#setup 
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

#game = Game()

sprites_nave = pygame.sprite.Group()
nave_principal = Nave()
sprites_nave.add(nave_principal)

#loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed():
        if pygame.key.get_pressed()[pygame.K_UP]:
            nave_principal.move_up()
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            nave_principal.move_down()
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            nave_principal.move_left()
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            nave_principal.move_right()

    screen.fill('black')
    sprites_nave.update()
    sprites_nave.draw(screen)
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()