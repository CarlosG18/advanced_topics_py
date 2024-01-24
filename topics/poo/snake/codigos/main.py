import pygame
from snake.Snake import Snake

# pygame setup
pygame.init()
fonte = pygame.font.Font(None, 20)
tam_tela = 720
screen = pygame.display.set_mode((1280,tam_tela))
#screen = pygame.display.set_mode((tam_tela,tam_tela))
clock = pygame.time.Clock()
running = True

#criando a cobrinha
snake = Snake(1,5)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")


    if pygame.key.get_pressed()[pygame.K_DOWN]:
        snake.move_down()
    elif pygame.key.get_pressed()[pygame.K_UP]:
        snake.move_top()
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        snake.move_left()
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        snake.move_right()
    # RENDER YOUR GAME HERE
    snake.show(screen)
    snake.move()
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()