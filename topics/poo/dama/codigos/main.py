# Example file showing a basic pygame "game loop"
import pygame
from tabuleiro.peca import Peca
from tabuleiro.tabuleiro import Tabuleiro

# pygame setup
pygame.init()
fonte = pygame.font.Font(None, 36)
tam_tela = 720
#screen = pygame.display.set_mode((1280,tam_tela))
screen = pygame.display.set_mode((tam_tela,tam_tela))
clock = pygame.time.Clock()
running = True

tabuleiro = Tabuleiro(screen.get_width(),(0,153,0),(200,0,0))

def escrever_texto(texto, x, y, cor):
    # Renderiza o texto em uma superfície
    texto_superficie = fonte.render(texto, True, cor)  # Cor do texto: preto
    # Blita (desenha) a superfície de texto na tela
    screen.blit(texto_superficie, (x, y))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        tabuleiro.check_click(pygame.mouse.get_pos())
        pygame.time.wait(200)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    tabuleiro.show(screen)    
    '''
    pygame.draw.rect(screen, "black", pygame.Rect(740,20,520,680))
    escrever_texto(f'player 1 : cor preto', 850, 100, "yellow")
    escrever_texto(f'player 2 : cor branco', 850, 200, "yellow")
    escrever_texto(f'movimento: player {tabuleiro.prox_jogada}', 850, 300, (255,255,255))
    '''
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()