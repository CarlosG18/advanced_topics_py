from snake.Snake import Snake, BadSnake, GoodSnake
from background.Background import Background
from food.Food import Food
import random
from game.Tela import TelaInfos, TelaGameOver, TelaInicio
from game.Bosters import Bosters

class Game:
    def __init__(self, screen):
        self.start = False
        self.background = Background(1000,720)
        self.snake = Snake(2,10, self.background.matriz_elemet)
        self.snake_died = False
        self.apple = self.create_apple()
        self.screen = screen
        self.tela = TelaInfos(screen,20)
        self.nivel = 1
        self.movimentos = 50
        self.vidas = 3
        self.cont_eat = 0
        self.boster = None
        self.status_buttons = None
        self.tela_game_over = TelaGameOver(self.screen,70)
        self.tela_init = TelaInicio(screen,30)
        #self.badsnake = BadSnake(2,10,self.background.matriz_elemet)

    def create_boster(self):
            i = random.randint(0,self.background.linhas-1)
            j = random.randint(0,self.background.colunas-1)
            x, y = self.background.get_xy(i,j)
            self.boster = Bosters("./assets/Graphics/tail_down.png",x,y,i,j,"movimento+")

    def show_boster(self):
            self.boster.show(self.screen)

    def tela_inicio(self):
        self.tela_init.show()
        self.tela_init.set_tam_font(120)
        self.tela_init.write("SNAKEBRAIN", 350, 150,(0,0,255))
        self.tela_init.set_tam_font(20)
        self.tela_init.write("como jogar: ",135, 450,(255,0,0))
        self.tela_init.write("voce tem inicialmente 50 movimentos para usar, um boster de mais 25 jogadas sera dropado em um lugar aleatorio",250, 450,(0,0,0))
        self.tela_init.write("a cada 2 macas capturadas. cada nivel voce tera que capturar um numero definido de macas para passar de fase. voce ",250, 475,(0,0,0))
        self.tela_init.write("tera 3 vidas em cada nivel e se seus movimentos chegarem a 0 voce perdera uma vida. o jogo possui 10 fases.",250, 500,(0,0,0))

    def infos_tela(self):
        self.tela.show()
        self.tela.write(f"NIVEL = {self.nivel}",1050,20, (0,0,0))
        self.tela.write(f"VIDAS = {self.vidas}",1050,40, (0,0,0))
        self.tela.write(f"MOVIMENTOS = {self.movimentos}",1050,60, (0,0,0))
        self.tela.write(f"TAMANHO = {self.snake.tamanho}",1050,80, (0,0,0))

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
            self.snake_died = self.snake.check_died()
            if self.movimentos == 0:
                self.snake_died = True
            if self.snake_died:
                self.tela_morreu()
        #self.badsnake.move_auto()
            
    def show_background(self):
        self.background.show(self.screen)
        if not self.start:
            self.tela_inicio()
        if self.boster:
            self.show_boster()

    def show_snake(self):
        if not self.snake_died and self.start:
            self.infos_tela()
            self.snake.show(self.screen)
            #self.badsnake.show(self.screen)
    
    def show_apple(self):
        if not self.snake_died and self.start:
            self.apple.show(self.screen)

    def check_eat(self):
        comeu = self.snake.check_eat(self.apple)
        comeu_boster = self.snake.check_eat_boster(self.boster)
        if comeu_boster:
            self.movimentos += 25
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
    
    def check_click_button(self, x, y):
        if not self.start:
            dados = self.tela_init.check_click(x,y)
        else:
            if self.snake_died:
                dados = self.tela_game_over.check_click(x,y)
            else:
                dados = self.tela.check_click(x,y)
        self.status_buttons = dados

        if self.status_buttons is not None:
            for btn in self.status_buttons:
                if btn["function"] == "restart" and btn["status"] == True:
                    self.reiniciar_game()
                elif btn["function"] == "pause" and btn["status"] == True:
                    self.pause_game()
                elif btn["function"] == "start" and  btn["status"] == True:
                    self.init_game()
                    

    def reiniciar_game(self):
        self.snake_died = False
        self.snake = Snake(2,10, self.background.matriz_elemet)
        self.apple = self.create_apple()
        self.nivel = 1
        self.movimentos = 50
        self.vidas = 3
        self.cont_eat = 0
        self.boster = None
        self.status_buttons = None

    def pause_game(self):
        print("pause o jogo!")
    
    def init_game(self):
        self.start = True

    def tela_morreu(self):
        self.tela_game_over.show()
        self.tela_game_over.write("Game Over!",480,250,"black")