from .Element import Head, Body, Tail
import pygame

class Snake:
    def __init__(self, tamanho, velo, vetor_posicoes):
        self.tamanho = tamanho
        self.velo = velo
        self.direcao = None
        self.head = None
        self.corpo = []
        self.last_pos = None
        self.matriz_posicoes = self.get_vetor_posicoes(vetor_posicoes)
        self.create_snake()

    def get_vetor_posicoes(self, vetor_elemet):
        matriz = []
        for elemento_linha in vetor_elemet:
            linha_matriz = []
            for elemento_coluna in elemento_linha:
                posicao = {
                    "x": elemento_coluna.y,
                    "y": elemento_coluna.x,
                }
                linha_matriz.append(posicao)
            matriz.append(linha_matriz)
        return matriz
            

    def create_snake(self):
        self.head = Head(self.matriz_posicoes[0][0]["x"],self.matriz_posicoes[0][0]["y"], 0, 0, None)
        self.corpo.append(self.head)
        for j in range(1, self.tamanho):
            body = Body(self.matriz_posicoes[0][j]["x"],self.matriz_posicoes[0][j]["y"], 0, j, "left")
            self.corpo.append(body)
        rabo = Tail(self.matriz_posicoes[0][self.tamanho]["x"],self.matriz_posicoes[0][self.tamanho]["y"], 0, self.tamanho, "left")
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
                


    def move_body(self):
        for index in range(1, len(self.corpo)):
            if self.corpo[index].direction_prox_ele == "left":
                if self.corpo[index].j - 1 >= 0:
                    self.corpo[index].j -= 1
                else:
                    self.corpo[index].j = len(self.matriz_posicoes[0])-1
                self.corpo[index].update_pos(self.matriz_posicoes)
            elif self.corpo[index].direction_prox_ele == "right":
                if self.corpo[index].j + 1 <= len(self.matriz_posicoes[0])-1:
                    self.corpo[index].j += 1
                else:
                    self.corpo[index].j = 0
                self.corpo[index].update_pos(self.matriz_posicoes)
            elif self.corpo[index].direction_prox_ele == "up":
                if self.corpo[index].i - 1 >= 0:
                    self.corpo[index].i -= 1
                else:
                    self.corpo[index].i = len(self.matriz_posicoes)-1
                self.corpo[index].update_pos(self.matriz_posicoes)
                
            elif self.corpo[index].direction_prox_ele == "down":
                if self.corpo[index].i + 1 <= len(self.matriz_posicoes)-1:
                    self.corpo[index].i += 1
                else:
                    self.corpo[index].i = 0
                self.corpo[index].update_pos(self.matriz_posicoes)
        self.update_direction()

    def move(self):
        #j == movimento de colunas
        #i == movimento de linhas

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

    def move_top(self):
        self.direcao = "up"
        self.corpo[0].troca_img_element("./assets/Graphics/head_up.png")
    
    def move_left(self):
        self.direcao = "left"
        self.corpo[0].troca_img_element("./assets/Graphics/head_left.png")

    def move_down(self):
        self.direcao = "down"
        self.corpo[0].troca_img_element("./assets/Graphics/head_down.png")

    def move_right(self):
        self.direcao = "right"
        self.corpo[0].troca_img_element("./assets/Graphics/head_right.png")

    def print_snake(self):
        for elemento_snake in self.corpo:
            print(elemento_snake)

    def print_pos_head(self):
        print(f'x = {self.head.i}, y = {self.head.j}')

    