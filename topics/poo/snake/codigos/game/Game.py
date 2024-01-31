from snake.Snake import Snake
from background.Background import Background
from food.Food import Food
import random

class Game:
    def __init__(self, width_tela, height_tela):
        self.background = Background(width_tela,height_tela)
        self.snake = Snake(2,10, self.background.matriz_elemet)
        self.apple = self.create_apple()
        self.buffer_directions = ["left"]
        self.cont_eat = 0

    def add_buffer_directions(self, direcao):
        self.buffer_directions.append(direcao)
        for index, direcao in enumerate(self.buffer_directions):
            print(f'buffer[{index}]={direcao}')
        print("\n")

    def move_snake(self):
        direcao = self.buffer_directions[0]
        if len(self.buffer_directions) > 1:
            self.buffer_directions.pop(0)

        if direcao == "left":
            self.snake.move_left()
        elif direcao == "right":
            self.snake.move_right()
        elif direcao == "up":
            self.snake.move_top()
        elif direcao == "down":
            self.snake.move_down()
        self.snake.move()
            
    def show_background(self, screen):
        self.background.show(screen)

    def show_snake(self, screen):
        self.snake.show(screen)
    
    def show_apple(self, screen):
        self.apple.show(screen)

    def check_eat(self):
        comeu = self.snake.check_eat(self.apple)
        #print(f'comeu = {comeu}')
        if comeu:
            self.apple = self.create_apple()
            self.cont_eat += 1
            if self.cont_eat == 5:
                self.cont_eat = 0
                self.snake.deset_velo()

    def create_apple(self):
        linha = random.randint(0,self.background.linhas-1)
        coluna = random.randint(0,self.background.colunas-1)
        #print(f'linha = {linha}, coluna = {coluna}')
        return Food("./assets/Graphics/apple.png",self.background.matriz_elemet[linha][coluna].x, self.background.matriz_elemet[linha][coluna].y, linha, coluna)