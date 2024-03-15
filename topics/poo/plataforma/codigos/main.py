import pygame
from personagem.Personagem import Personagem
from cenario.Cenario import Cenario
import random
from edit.Editar import Editar

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

'''
matriz_cenario = []
for i in range(22):
    linha = []
    for j in range(40):
        elemento = random.randint(0,1)
        linha.append(elemento)
    matriz_cenario.append(linha)
'''
edit = Editar()

#print(matriz_cenario)

heroi = Personagem()
cenario = Cenario(edit.matriz,heroi)

while running:
    # poll for events
    screen.fill("black")
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        i,j = edit.get_ij_click(pygame.mouse.get_pos())
        edit.criar_elemento(i,j)
        cenario.update_matriz(edit.matriz)

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        pass
        heroi.walk("right")
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        pass
        heroi.walk("left")
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        pass
    if pygame.key.get_pressed()[pygame.K_UP]:
        pass
        heroi.fly()

    heroi.show(screen)

    cenario.show(screen)
    edit.show(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(30)  # limits FPS to 60

pygame.quit()