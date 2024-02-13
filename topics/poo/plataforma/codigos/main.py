import pygame
from personagem.Personagem import Personagem, Animacao
from pygame.sprite import Group

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

heroi = Personagem()

while running:
    # poll for events
    screen.fill("black")
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        heroi.walk("right")
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        heroi.walk("left")
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        pass
    if pygame.key.get_pressed()[pygame.K_UP]:
        heroi.fly()

    heroi.show(screen)
    heroi.gravidade()
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(30)  # limits FPS to 60

pygame.quit()