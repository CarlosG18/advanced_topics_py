import pygame
from snake.Snake import Snake
from background.Background import Background

# pygame setup
pygame.init()
fonte = pygame.font.Font(None, 20)
tam_tela = 720
screen = pygame.display.set_mode((1280,tam_tela))
#screen = pygame.display.set_mode((tam_tela,tam_tela))
clock = pygame.time.Clock()
running = True

#criando o backgroud
background = Background(1280,720)

#criando a cobrinha
snake = Snake(10,10,background.vetor_elemet)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background.show(screen)

    if pygame.mouse.get_pressed()[0]:
        background.print_element()
        snake.print_snake()

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        snake.move_down()
        print("baixo")
    elif pygame.key.get_pressed()[pygame.K_UP]:
        snake.move_top()
        print("up")
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        snake.move_left()
        print("left")

    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        snake.move_right()
        print("down")

        
    # RENDER YOUR GAME HERE
    snake.show(screen)
    snake.move()
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(1)  # limits FPS to 60

pygame.quit()