from snake.Snake import Snake
from background.Background import Background
from food.Food import Food
import random
from game.Tela import TelaInfos, TelaGameOver, TelaInicio
from game.Bosters import Bosters
from game.Nivel import Nivel
import pygame

def load_music(caminho):
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

class Game:
    def __init__(self, screen):
        self.start = False
        self.background = Background(1000,720)
        self.snake = Snake(2,10, self.background.matriz_elemet)
        self.snake_died = False
        self.apple = self.create_apple()
        self.screen = screen
        self.tela = TelaInfos(screen,20)
        self.movimentos = 50
        self.vidas = 3
        self.deset_vidas = False
        self.cont_eat = 0
        self.boster = None
        self.boster_invisible = None
        self.bosters = []
        self.status_buttons = None
        self.tela_game_over = TelaGameOver(self.screen,70)
        self.tela_init = TelaInicio(screen,30)
        self.niveis = Nivel()
        self.snake_fatasma = False
        self.moves_fantasma = 20

    def check_empty_casa(self, i, j):
        empty = True
        for body in self.snake.corpo:
            if body.i == i and body.j == j:
                empty = False
                break
        return empty

    def create_boster(self, function):
            i = random.randint(0,self.background.linhas-1)
            j = random.randint(0,self.background.colunas-1)
            empty_casa = self.check_empty_casa(i,j)
            while not empty_casa:
                i = random.randint(0,self.background.linhas-1)
                j = random.randint(0,self.background.colunas-1)
                empty_casa = self.check_empty_casa(i,j)    
            x, y = self.background.get_xy(i,j)
            if function == "movimento+":
                boster_movimento = Bosters("./assets/Graphics/adicionar.png",x,y,i,j,"movimento+")
                #self.boster = Bosters("./assets/Graphics/adicionar.png",x,y,i,j,"movimento+")
                self.bosters.append(boster_movimento)
            elif function == "invisible":
                boster_invisible = Bosters("./assets/Graphics/fantasma.png",x,y,i,j,"invisible")
                self.bosters.append(boster_invisible)

    def show_boster(self):
        for boster in self.bosters:
            boster.show(self.screen)

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
        self.tela.set_tam_font(30)
        self.tela.write(f"NIVEL",1110,20, (255,255,255))
        self.tela.set_tam_font(100)
        self.tela.write(f'{self.niveis.nivel_atual}',1120,50, (255,255,255))
        self.tela.set_tam_font(30)
        self.tela.write(f"VIDAS",1110,190, (255,255,255))
        if self.vidas == 2 and self.deset_vidas:
            self.tela.modelife2()
            self.deset_vidas = False
        elif self.vidas == 1 and self.deset_vidas:
            self.tela.modelife1()
            self.deset_vidas = False
        self.tela.show_imgs()
        self.tela.write(f"MOVIMENTOS",1070,330, (255,255,255))
        self.tela.set_tam_font(100)
        self.tela.write(f"{self.movimentos}",1100,360, (255,255,255))
        self.tela.set_tam_font(30)
        self.tela.write(f"macas restantes",1050,520, (255,255,255))
        self.tela.set_tam_font(100)
        self.tela.write(f"{self.niveis.total_macas}",1100,550, (255,255,255))
        if self.snake_fatasma:
            self.tela.set_tam_font(15)
            self.tela.write(f"jogadas fantasmas restantes = {self.moves_fantasma}",1050,500, (255,255,255))    

    def deset_movimentos(self):
        self.movimentos -= 1
        if self.movimentos == 0:
            self.vidas -= 1
            self.deset_vidas = True
            self.movimentos = 50

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
            
            if self.snake.flag_move:
                self.snake.move()
                self.deset_movimentos()
                if not self.snake_fatasma:
                    self.snake_died = self.snake.check_died()
                else:
                    self.moves_fantasma -= 1
                    if self.moves_fantasma == 0:
                        self.snake_fatasma = False
                        self.moves_fantasma = 20
                
                if self.vidas == 0:
                    self.snake_died = True
                if self.snake_died:
                    self.tela_morreu()
                
    def show_background(self):
        self.screen.fill("black")
        self.background.show(self.screen)
        if not self.start:
            self.tela_inicio()
        if self.bosters:
            self.show_boster()

    def show_snake(self):
        if not self.snake_died and self.start:
            self.infos_tela()
            self.snake.show(self.screen)
    
    def show_apple(self):
        if not self.snake_died and self.start:
            self.apple.show(self.screen)

    def check_eat(self):
        #verificando os bosters
        if not self.bosters == []:
            for boster in self.bosters:
                comeu_boster = self.snake.check_eat_boster(boster)
                if comeu_boster:
                    if comeu_boster["function"] == "movimento+":
                        load_music(f"./assets/musics/boster_eat.mp3")
                        self.movimentos += 25
                        self.bosters.remove(boster) 
                    elif comeu_boster["function"] == "invisible":
                        load_music(f"./assets/musics/boster_eat.mp3")
                        self.bosters.remove(boster)
                        self.snake_fatasma = True

        #verificando a maca
        comeu = self.snake.check_eat(self.apple)
        if comeu:
            self.niveis.snake_eat()
            if self.niveis.total_macas == 0:
                self.niveis.up_nivel()
                self.reiniciar_game()
            load_music(f"./assets/musics/snake_eat.mp3")
            self.apple = self.create_apple()
            self.cont_eat += 1
            if self.cont_eat % 2 == 0:
                self.create_boster("movimento+")
            if self.cont_eat % 10 == 0:
                self.create_boster("invisible")

    def create_apple(self):
        linha = random.randint(0,self.background.linhas-1)
        coluna = random.randint(0,self.background.colunas-1)
        empty_casa = self.check_empty_casa(linha,coluna)
        while not empty_casa:
            linha = random.randint(0,self.background.linhas-1)
            coluna = random.randint(0,self.background.colunas-1)
            empty_casa = self.check_empty_casa(linha,coluna)  
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
        self.tela.modelife3()
        self.cont_eat = 0
        self.boster = None
        self.status_buttons = None

    def pause_game(self):
        print("pause o jogo!")
    
    def init_game(self):
        self.start = True

    def tela_morreu(self):
        self.tela_game_over.show()
        self.niveis.restart()
        efeitos_sonoros = ["tema-triste-toguro", "naruto-sad"]
        load_music(f"./assets/musics/{random.choice(efeitos_sonoros)}.mp3")
        self.tela_game_over.write("Game Over!",480,250,"black")