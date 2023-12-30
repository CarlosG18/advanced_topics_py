import pygame
from .casa import Casa
from .peca import Peca

class Tabuleiro:
    def __init__(self, tam, cor1, cor2):
        self.tam = tam
        self.cor1 = cor1
        self.cor2  = cor2
        self.casas_matriz = []
        self.pecas_player1 = []
        self.pecas_player2 = []
        self.matriz_pos = []
        self.tam_casa = None
        self.prox_jogada = 1
        self.modo = "select"
        self.casa_atual = None
        self.ajust_tam()
        self.create_casas()
        self.click = False

    def set_prox_jogada(self):
        if self.prox_jogada == 1:
            self.prox_jogada = 2
        else:
            self.prox_jogada = 1
    
    def set_click(self):
        self.click = not(self.click)

    def ajust_tam(self):
        if self.tam > 720:
            self.tam = 720

    def create_casas(self):
        #set configurações de cada casa
        self.tam_casa = int(self.tam/8)

        for i in range(8):
            row_matriz = []
            row_matriz_pos = []
            for j in range(8):
                if (i+j) % 2 == 0:
                    cor = self.cor2
                else:
                    cor = self.cor1
                casa = Casa(i,j,self.tam_casa*j,self.tam_casa*i,self.tam_casa,self.tam_casa,cor)
                element_pos = {
                    "x": casa.x + (self.tam_casa/2),
                    "y": casa.y + (self.tam_casa/2)
                }
                row_matriz.append(casa)
                row_matriz_pos.append(element_pos)
            self.casas_matriz.append(row_matriz)
            self.matriz_pos.append(row_matriz_pos)
        self.create_pecas()

    def create_pecas(self):
        #criando as pecas do player 1
        for i in range(3):
            for j in range(8):
                if self.casas_matriz[i][j].color == self.cor1:
                    peca = Peca(self.matriz_pos[i][j]["x"],self.matriz_pos[i][j]["y"],self.tam_casa/2 - (self.tam_casa/6),(0,0,0),1)
                    peca.player = 1
                    self.casas_matriz[i][j].set_ocupado(peca)
                    self.casas_matriz[i][j].player = 1
                    #self.pecas_player1.append(self.casas_matriz[i][j])
                #print(f'casa[{i}][{j}] (x={self.matriz_pos[i][j]["x"]}, y={self.matriz_pos[i][j]["y"]}) cor = {self.casas_matriz[i][j]["casa"].color}')

        #criando as pecas do player 2
        for i in range(5,8):
            for j in range(8):
                if self.casas_matriz[i][j].color == self.cor1:
                    peca = Peca(self.matriz_pos[i][j]["x"],self.matriz_pos[i][j]["y"],self.tam_casa/2 - (self.tam_casa/6),(255,255,255),1)
                    peca.player = 2
                    self.casas_matriz[i][j].set_ocupado(peca)
                    self.casas_matriz[i][j].player = 1
                    #self.pecas_player2.append(self.casas_matriz[i][j])
            

    def show(self, screen):
        for i in range(8):
            for j in range(8):
                #print(f'casa[{i}][{j}] (x={self.casas_matriz[i][j]["casa"].x}, y={self.casas_matriz[i][j]["casa"].y}) cor = {self.casas_matriz[i][j]["casa"].color}')
                self.casas_matriz[i][j].create(screen)
                if self.casas_matriz[i][j].ocupado is not None:
                    self.casas_matriz[i][j].ocupado.show(screen)

    def get_casa_click(self, pos):
        col = int(pos[0]/self.tam_casa)
        row = int(pos[1]/self.tam_casa)
        return (row, col)
    
    def get_peca(self, player, i, j):
        if player == 1:
            for peca in self.pecas_player1:
                if peca.i == i and peca.j == j:
                    return peca
        else:
            for peca in self.pecas_player2:
                if peca.i == i and peca.j == j:
                    return peca

    def set_modo(self):
        if self.modo == "select":
            self.modo = "move"
        else:
            self.modo = "select"
        
    def atualizar_matriz_casas(self, i, j):
        self.casas_matriz[i][j] = self.casa_atual

    def check_click(self, pos, screen):
        i, j = self.get_casa_click(pos)
        casa = self.casas_matriz[i][j]
        print(self.modo)
        print(f'casa selecionada {casa} - casa atual {self.casa_atual}')

        if self.modo == "select":
            if casa.ocupado:
                self.casa_atual = self.casas_matriz[i][j]
                if casa.ocupado.player == self.prox_jogada:
                    self.show_jogadas(casa)
            self.modo = "move"
        elif self.modo == "move":
            if casa.disponivel:
                self.casa_atual.ocupado.posX = self.matriz_pos[i][j]["x"]
                self.casa_atual.ocupado.posY = self.matriz_pos[i][j]["y"]
                casa.ocupado = self.casa_atual.ocupado
                self.casa_atual.ocupado = None
                self.atualizar_matriz_casas(self.casa_atual.i,self.casa_atual.j)
                casa.disponivel = False
                self.set_prox_jogada()
                self.reset()
            self.modo = "select"
            
    
    def show_jogadas(self, casa):
        i_prox = [casa.i-1,casa.i-1,casa.i+1,casa.i+1]
        j_prox = [casa.j-1,casa.j+1,casa.j-1,casa.j+1]

        for i in range(4):
            if self.casas_matriz[i_prox[i]][j_prox[i]].ocupado == None:
                self.casas_matriz[i_prox[i]][j_prox[i]].disponivel = True
                self.casas_matriz[i_prox[i]][j_prox[i]].color = "yellow"

    def reset(self):
        pass


        