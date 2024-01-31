from snake.Snake import Snake
from background.Background import Background
from food.Food import Food
import random

class Game:
    def __init__(self, width_tela, height_tela, tam_snake, velo_snake):
        self.background = Background(width_tela,height_tela)
        self.snake = Snake(tam_snake,velo_snake, self.background.matriz_elemet)
        self.apple = self.create_apple()
        
    def show_background(self, screen):
        self.background.show(screen)

    def show_snake(self, screen):
        self.snake.show(screen)
    
    def show_apple(self, screen):
        self.apple.show(screen)

    def check_eat(self):
        comeu = self.snake.check_eat(self.apple)
        print(f'comeu = {comeu}')
        if comeu:
            self.apple = self.create_apple()

    def create_apple(self):
        linha = random.randint(0,self.background.linhas-1)
        coluna = random.randint(0,self.background.colunas-1)
        #print(f'linha = {linha}, coluna = {coluna}')
        return Food("./assets/Graphics/apple.png",self.background.matriz_elemet[linha][coluna].x, self.background.matriz_elemet[linha][coluna].y, linha, coluna)