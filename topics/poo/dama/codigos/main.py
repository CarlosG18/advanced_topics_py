# Example file showing a basic pygame "game loop"
import pygame
from tabuleiro.peca import Peca
from tabuleiro.tabuleiro import Tabuleiro

# pygame setup
pygame.init()
fonte = pygame.font.Font(None, 20)
tam_tela = 720
screen = pygame.display.set_mode((1280,tam_tela))
#screen = pygame.display.set_mode((tam_tela,tam_tela))
clock = pygame.time.Clock()
running = True

img_player = pygame.image.load('./assets/controle.png')
img_player_rect = img_player.get_rect()
#definindo a posição da imagem do player
img_player_rect.x = 860
img_player_rect.y = 50

img_player2 = pygame.image.load('./assets/controle.png')
img_player_rect2 = img_player.get_rect()
#definindo a posição da imagem do player
img_player_rect2.x = 860
img_player_rect2.y = 125

#definindo a img da seta
seta = pygame.image.load('./assets/arrow.png')
seta = pygame.transform.scale(seta, (32,32))
seta_rect = img_player.get_rect()
seta_rect.x = 1160

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
        if pygame.mouse.get_pos()[0] <= 720:
            tabuleiro.check_click(pygame.mouse.get_pos())
            pygame.time.wait(200)
        print(pygame.mouse.get_pos())

    

    # RENDER YOUR GAME HERE
    tabuleiro.show(screen)    

    #tabela de informações sobre o jogo    
    pygame.draw.rect(screen, (200,200,200), pygame.Rect(740,20,520,680))
    pygame.draw.lines(screen, (0,0,0), True, [(760,40),(1240,40),(1240,680),(760,680)])
    screen.blit(img_player, img_player_rect)
    escrever_texto(f'player 1 : cor preto', 940, 70, "black")
    screen.blit(img_player2, img_player_rect2)
    escrever_texto(f'player 2 : cor branco', 940, 145, "black")
    
    if tabuleiro.prox_jogada == 1:
        seta_rect.y = 65
    else:
        seta_rect.y = 140
    screen.blit(seta, seta_rect)
    
    if tabuleiro.peca_kill:
        escrever_texto(f'Peça a ser capturada {tabuleiro.peca_kill}', 780, 200, "black")
    else:
        escrever_texto(f'Nenhuma peça a ser capturada', 780, 200, "black")
    
    escrever_texto(f'casas disponiveis:', 780, 230, "black")
    if tabuleiro.casas_dispo:
        for index, casa in enumerate(tabuleiro.casas_dispo):
            escrever_texto(f'casas disponivel {casa}', 780, 250+(index*20), "black")
    else:
        escrever_texto(f'nenhuma casa disponivel', 780, 250, "red")

    escrever_texto(f'pecas prioritarias:', 780, 310, "black")
    if tabuleiro.priority:
        for index, casa in enumerate(tabuleiro.priority):
            escrever_texto(f'casas prioritaria {casa}', 780, 340+(index*20), "black")
    else:
        escrever_texto(f'nenhuma peça prioritaria', 780, 340, "red")

    if tabuleiro.casa_atual:
        escrever_texto(f'Peça atual selecionada na {tabuleiro.casa_atual}', 780, 380, "black")
    else:
        escrever_texto(f'Nenhuma peça selecionada', 780, 380, "black")

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()