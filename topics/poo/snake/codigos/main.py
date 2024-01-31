import pygame
from snake.Snake import Snake
from background.Background import Background
from food.Food import Food
from game.Game import Game

# pygame setup
pygame.init()
fonte = pygame.font.Font(None, 20)
tam_tela = 720
screen = pygame.display.set_mode((1280,tam_tela))
#screen = pygame.display.set_mode((tam_tela,tam_tela))
clock = pygame.time.Clock()
running = True

game = Game(1280,tam_tela)
cont = 0

#criando o backgroud
#background = Background(1280,720)

#criando o alimento
#apple = Food("./assets/Graphics/apple.png",background.matriz_elemet[5][5].x,background.matriz_elemet[5][5].y,5,5)

#criando a cobrinha
#snake = Snake(2,10,background.matriz_elemet)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.show_background(screen)

    
    if pygame.mouse.get_pressed()[0]:
        pass

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        #game.snake.move_down()      
        game.add_buffer_directions("down")
        #game.snake.move()
        #game.snake.check_eat(game.apple)
        pygame.time.wait(100)
    elif pygame.key.get_pressed()[pygame.K_UP]:
        #game.snake.move_top()
        game.add_buffer_directions("up")
        #game.snake.move()
        #game.snake.check_eat(game.apple)
        pygame.time.wait(100)
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        #game.snake.move_left()
        game.add_buffer_directions("left")
        #game.snake.move()
        #game.snake.check_eat(game.apple)
        pygame.time.wait(100)
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        #game.snake.move_right()
        game.add_buffer_directions("right")
        #game.snake.move()
        
        #game.snake.check_eat(game.apple)
        pygame.time.wait(100)
    
        
    # RENDER YOUR GAME HERE
    game.show_snake(screen)
    game.show_apple(screen)
    cont += 1
    if cont == game.snake.velo:
        game.move_snake()
        cont = 0
    game.check_eat()

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()