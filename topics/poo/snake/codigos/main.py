import pygame
from snake.Snake import Snake
from background.Background import Background
from food.Food import Food
from game.Game import Game

# pygame setup
pygame.init()
tam_tela = 720
screen = pygame.display.set_mode((1280,tam_tela))
#screen = pygame.display.set_mode((tam_tela,tam_tela))
clock = pygame.time.Clock()
running = True

game = Game(screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
            game.check_click_button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

    if not game.snake_died:
        game.show_background()

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            game.move_snake("down")
            game.check_eat()
            pygame.time.wait(150)
        elif pygame.key.get_pressed()[pygame.K_UP]:
            game.move_snake("up")
            game.check_eat()
            pygame.time.wait(150)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            game.move_snake("left")
            game.check_eat()
            pygame.time.wait(150)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            game.move_snake("right")
            game.check_eat()
            pygame.time.wait(150)

        game.show_snake()
        game.show_apple()    

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()