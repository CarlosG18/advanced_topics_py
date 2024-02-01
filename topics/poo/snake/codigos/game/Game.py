from snake.Snake import Snake
from background.Background import Background
from food.Food import Food
import random
from game.Tela import Tela
from game.Bosters import Bosters

class Game:
    def __init__(self, screen, fonte):
        self.background = Background(1000,720)
        self.snake = Snake(2,10, self.background.matriz_elemet)
        self.apple = self.create_apple()
        self.screen = screen
        self.tela = Tela(screen, fonte)
        self.nivel = 1
        self.movimentos = 50
        self.vidas = 3
        self.cont_eat = 0
        self.boster = None

    def create_boster(self):
            i = random.randint(0,self.background.linhas)
            j = random.randint(0,self.background.colunas)
            x, y = self.background.get_xy(i,j)
            self.boster = Bosters("./assets/Graphics/tail_down.png",x,y,i,j,"movimento+")

    def show_boster(self):
            self.boster.show(self.screen)

    def infos_tela(self):
        self.tela.show()
        self.tela.write(f"nivel = {self.nivel}",1050,20, (0,0,0))
        self.tela.write(f"vidas = {self.vidas}",1050,40, (0,0,0))
        self.tela.write(f"movimentos = {self.movimentos}",1050,60, (0,0,0))
        self.tela.write(f"tamanho = {self.snake.tamanho}",1050,80, (0,0,0))

    def deset_movimentos(self):
        self.movimentos -= 1

    def move_snake(self, direcao):
        if self.movimentos > 0:
            if direcao == "left":
                self.snake.move_left()
            elif direcao == "right":
                self.snake.move_right()
            elif direcao == "up":
                self.snake.move_top()
            elif direcao == "down":
                self.snake.move_down()
            self.snake.move()
            self.deset_movimentos()
            
    def show_background(self):
        self.background.show(self.screen)
        if self.boster:
            self.show_boster()

    def show_snake(self):
        self.snake.show(self.screen)
        self.infos_tela()
    
    def show_apple(self):
        self.apple.show(self.screen)

    def check_eat(self):
        comeu = self.snake.check_eat(self.apple)
        comeu_boster = self.snake.check_eat_boster(self.boster)
        if comeu_boster:
            self.movimentos += 50
            self.boster = None
        #print(f'comeu = {comeu}')
        if comeu:
            self.apple = self.create_apple()
            self.cont_eat += 1
            if self.cont_eat == 2:
                self.create_boster()
                self.cont_eat = 0

    def create_apple(self):
        linha = random.randint(0,self.background.linhas-1)
        coluna = random.randint(0,self.background.colunas-1)
        #print(f'linha = {linha}, coluna = {coluna}')
        return Food("./assets/Graphics/apple.png",self.background.matriz_elemet[linha][coluna].x, self.background.matriz_elemet[linha][coluna].y, linha, coluna)
    
    def reiniciar_game(self):
        pass