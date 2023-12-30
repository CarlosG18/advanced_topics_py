# Example file showing a basic pygame "game loop"
import pygame
from tabuleiro.peca import Peca
from tabuleiro.tabuleiro import Tabuleiro

# pygame setup
pygame.init()
tam_tela = 720
screen = pygame.display.set_mode((1280,tam_tela))
clock = pygame.time.Clock()
running = True

tabuleiro = Tabuleiro(screen.get_width(),(0,153,0),(200,0,0))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        tabuleiro.check_click(pygame.mouse.get_pos(), screen)
        pygame.time.wait(200)



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    tabuleiro.show(screen)    
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()