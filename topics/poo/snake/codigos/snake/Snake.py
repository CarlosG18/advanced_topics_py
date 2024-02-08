from .Element import Head, Body, Tail
import pygame
import random

class Snake:
    def __init__(self, tamanho, velo, vetor_posicoes):
        self.tamanho = tamanho
        self.velo = velo
        self.direcao = "left"
        self.head = None
        self.corpo = []
        self.last_pos = None
        self.matriz_posicoes = self.get_matriz_posicoes(vetor_posicoes)
        self.died = False
        self.flag_move = False
        self.create_snake()

    def get_matriz_posicoes(self, vetor_elemet):
        matriz = []
        for elemento_linha in vetor_elemet:
            linha_matriz = []
            for elemento_coluna in elemento_linha:
                posicao = {
                    "x": elemento_coluna.x,
                    "y": elemento_coluna.y,
                }
                linha_matriz.append(posicao)
            matriz.append(linha_matriz)
        return matriz
            

    def create_snake(self):
        index_i = random.randint(0, len(self.matriz_posicoes)-1)
        index_j = random.randint(0,len(self.matriz_posicoes[0])-1)
        while index_j + self.tamanho >= len(self.matriz_posicoes[0]):
            index_j = random.randint(0,len(self.matriz_posicoes[0])-1)
        
        self.head = Head(self.matriz_posicoes[index_i][index_j]["x"],self.matriz_posicoes[index_i][index_j]["y"], index_i, index_j, None)
        self.corpo.append(self.head)
        for j in range(1, self.tamanho):
            body = Body(self.matriz_posicoes[index_i][index_j+j]["x"],self.matriz_posicoes[index_i][index_j+j]["y"], index_i, index_j+j, "left")
            self.corpo.append(body)
        rabo = Tail(self.matriz_posicoes[index_i][self.tamanho+index_j]["x"],self.matriz_posicoes[index_i][self.tamanho+index_j]["y"], index_i, self.tamanho+index_j, "left")
        self.corpo.append(rabo)

    def update_corpo(self):
        self.corpo[0] = self.head

    def update_direction(self):
        for index in range(len(self.corpo)-1, 0, -1):
            if index - 1 >= 0:
                #troca do tail da snake
                if index == len(self.corpo)-1:
                    if self.corpo[index-1].direction_prox_ele == "left":
                        self.corpo[index].troca_img_element("./assets/Graphics/tail_right.png")
                    elif self.corpo[index-1].direction_prox_ele == "right":
                        self.corpo[index].troca_img_element("./assets/Graphics/tail_left.png")
                    elif self.corpo[index-1].direction_prox_ele == "up":
                        self.corpo[index].troca_img_element("./assets/Graphics/tail_down.png")
                    else:
                        self.corpo[index].troca_img_element("./assets/Graphics/tail_up.png")
                #troca do body
                else:
                    # troca do body nas viradas da snake
                    if self.corpo[index].direction_prox_ele != self.corpo[index-1].direction_prox_ele:
                        pass
                    # troca no body reto   
                    elif self.corpo[index].direction_prox_ele == "left" or self.corpo[index].direction_prox_ele == "right":
                        self.corpo[index].troca_img_element("./assets/Graphics/body_horizontal.png")
                    else:
                        self.corpo[index].troca_img_element("./assets/Graphics/body_vertical.png")

                self.corpo[index].direction_prox_ele = self.corpo[index-1].direction_prox_ele
                

    def check_curva(self, index):
        elemento_anterior = self.corpo[index-1]
        elemento_atual = self.corpo[index]

        if elemento_anterior.direction_prox_ele != elemento_atual.direction_prox_ele:
            if elemento_anterior.direction_prox_ele == "down":
                if elemento_atual.direction_prox_ele == "left":
                    self.corpo[index].troca_img_element("./assets/Graphics/body_bottomright.png")
                elif elemento_atual.direction_prox_ele == "right":
                    self.corpo[index].troca_img_element("./assets/Graphics/body_bottomleft.png")

            elif elemento_anterior.direction_prox_ele == "up":
                if elemento_atual.direction_prox_ele == "left":
                    self.corpo[index].troca_img_element("./assets/Graphics/body_topright.png")
                elif elemento_atual.direction_prox_ele == "right":
                    self.corpo[index].troca_img_element("./assets/Graphics/body_topleft.png")

            elif elemento_anterior.direction_prox_ele == "left":
                if elemento_atual.direction_prox_ele == "up":
                    self.corpo[index].troca_img_element("./assets/Graphics/body_bottomleft.png")
                elif elemento_atual.direction_prox_ele == "down":
                    self.corpo[index].troca_img_element("./assets/Graphics/body_topleft.png")

            elif elemento_anterior.direction_prox_ele == "right":
                if elemento_atual.direction_prox_ele == "up":
                    self.corpo[index].troca_img_element("./assets/Graphics/body_bottomright.png")
                elif elemento_atual.direction_prox_ele == "down":
                    self.corpo[index].troca_img_element("./assets/Graphics/body_topright.png")
            

    def move_body(self):
        for index in range(1, len(self.corpo)):
            if self.corpo[index].direction_prox_ele == "left":
                self.check_curva(index)
                if self.corpo[index].j - 1 >= 0:
                    self.corpo[index].j -= 1
                else:
                    self.corpo[index].j = len(self.matriz_posicoes[0])-1
                self.corpo[index].update_pos(self.matriz_posicoes)
            elif self.corpo[index].direction_prox_ele == "right":
                self.check_curva(index)
                if self.corpo[index].j + 1 <= len(self.matriz_posicoes[0])-1:
                    self.corpo[index].j += 1
                else:
                    self.corpo[index].j = 0
                self.corpo[index].update_pos(self.matriz_posicoes)
            elif self.corpo[index].direction_prox_ele == "up":
                self.check_curva(index)
                if self.corpo[index].i - 1 >= 0:
                    self.corpo[index].i -= 1
                else:
                    self.corpo[index].i = len(self.matriz_posicoes)-1
                self.corpo[index].update_pos(self.matriz_posicoes)
                
            elif self.corpo[index].direction_prox_ele == "down":
                self.check_curva(index)
                if self.corpo[index].i + 1 <= len(self.matriz_posicoes)-1:
                    self.corpo[index].i += 1
                else:
                    self.corpo[index].i = 0
                self.corpo[index].update_pos(self.matriz_posicoes)
        self.update_direction()
        self.last_pos = self.set_last_pos()
        #print(self.last_pos, "\n")


    def set_last_pos(self):
        last_elemento = self.corpo[self.tamanho]
        #print(f'last_corpo = {last_elemento}')
        #direita
        if last_elemento.direction_prox_ele == "left":
            return Body(last_elemento.x+50,last_elemento.y,last_elemento.i,last_elemento.j+1,last_elemento.direction_prox_ele)
        #esquerda
        elif last_elemento.direction_prox_ele == "right":
            return Body(last_elemento.x-50,last_elemento.y,last_elemento.i,last_elemento.j-1,last_elemento.direction_prox_ele)
        #baixo
        elif last_elemento.direction_prox_ele == "up":
            return Body(last_elemento.x,last_elemento.y+50,last_elemento.i+1,last_elemento.j,last_elemento.direction_prox_ele)
        #cima
        elif last_elemento.direction_prox_ele == "down":
            return Body(last_elemento.x,last_elemento.y-50,last_elemento.i-1,last_elemento.j,last_elemento.direction_prox_ele)


    def move(self):
        #j == movimento de colunas
        #i == movimento de linhas
        #pygame.time.wait(5*self.velo)

        if self.direcao == "left":
            self.head.direction_prox_ele = "left"
            if self.head.j - 1 >= 0:
                self.head.j -= 1
            else:
                self.head.j = len(self.matriz_posicoes[0])-1
            self.head.update_pos(self.matriz_posicoes)
            self.update_corpo()
        elif self.direcao == "right":
            self.head.direction_prox_ele = "right"
            if self.head.j + 1 <= len(self.matriz_posicoes[0])-1:
                self.head.j += 1
            else:
                self.head.j = 0
            self.head.update_pos(self.matriz_posicoes)
            self.update_corpo()
        elif self.direcao == "up":
            self.head.direction_prox_ele = "up"
            if self.head.i - 1 >= 0:
                self.head.i -= 1
            else:
                self.head.i = len(self.matriz_posicoes)-1
            self.head.update_pos(self.matriz_posicoes)
            self.update_corpo()
        elif self.direcao == "down":
            self.head.direction_prox_ele = "down"
            if self.head.i + 1 <= len(self.matriz_posicoes)-1:
                self.head.i += 1
            else:
                self.head.i = 0
            self.head.update_pos(self.matriz_posicoes)
            self.update_corpo()
        self.last_pos = (self.head.i,self.head.j)
        self.move_body()
 
    def show(self, screen):
        for element in self.corpo:
            element.show(screen)

    def att_corpo(self, elemento, index):
        new_body = Body(elemento.x,elemento.y,elemento.i,elemento.j,elemento.direction_prox_ele)
        self.corpo[index] = new_body

    def check_eat(self,apple):
        if self.head.i == apple.i and self.head.j == apple.j:
            elemento = self.corpo[len(self.corpo)-1]
            self.att_corpo(elemento, len(self.corpo)-1)
            self.corpo.append(Tail(self.last_pos.x,self.last_pos.y,self.last_pos.i,self.last_pos.j,self.last_pos.direction_prox_ele))
            self.tamanho += 1
            return True
        else:
            return False

    def check_died(self):
        for index in range(1,len(self.corpo)):
            if self.head.i == self.corpo[index].i and self.head.j == self.corpo[index].j:
                return True
        return False
    
    def check_eat_boster(self, elemento):
        if elemento is not None:
            if self.head.i == elemento.i and self.head.j == elemento.j:
                dados = {
                    "status": True,
                    "function": elemento.function
                }
                return dados
            else:
                return False
        else:
            return False  

    def move_top(self):
        if self.direcao != "down":
            self.direcao = "up"
            self.corpo[0].troca_img_element("./assets/Graphics/head_up.png")
            self.flag_move = True
        else:
            self.flag_move = False
    
    def move_left(self):
        if self.direcao != "right":
            self.direcao = "left"
            self.corpo[0].troca_img_element("./assets/Graphics/head_left.png")
            self.flag_move = True
        else:
            self.flag_move = False

    def move_down(self):
        if self.direcao != "up":
            self.direcao = "down"
            self.corpo[0].troca_img_element("./assets/Graphics/head_down.png")
            self.flag_move = True
        else:
            self.flag_move = False

    def move_right(self):
        if self.direcao != "left":
            self.direcao = "right"
            self.corpo[0].troca_img_element("./assets/Graphics/head_right.png")
            self.flag_move = True
        else:
            self.flag_move = False

    def print_snake(self):
        for elemento_snake in self.corpo:
            print(elemento_snake)
        print("\n")

    def print_pos_head(self):
        print(f'x = {self.head.i}, y = {self.head.j}')

    def deset_velo(self):
        if self.velo - 1 > 0:
            self.velo -= 1

    

class BadSnake(Snake):
    def __init__(self, tamanho, velo, vetor_posicoes):
        super().__init__(tamanho, velo, vetor_posicoes)
        self.movimentos = 5

    def move_auto(self):
        if self.movimentos == 5:
            direcoes = ['up','down','left','right']
            direcao = random.choices(direcoes)
            self.direcao = direcao[0]

        if self.movimentos-1 >= 0:
            self.movimentos -= 1
        else:
            self.movimentos = 5

        if self.direcao == 'left':
            self.move_left()
        elif self.direcao == 'right':
            self.move_right()
        elif self.direcao == 'up':
            self.move_top()
        elif self.direcao == 'down':
            self.move_down()
        self.move()

class GoodSnake(Snake):
    def __init__(self, tamanho, velo, vetor_posicoes):
        super().__init__(tamanho, velo, vetor_posicoes)

     
        