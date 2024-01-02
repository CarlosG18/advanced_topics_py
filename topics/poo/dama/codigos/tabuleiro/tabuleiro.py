import pygame
from .casa import Casa
from .peca import Peca

def load_music(caminho):
    pygame.mixer.music.load(caminho)

class Tabuleiro:
    def __init__(self, tam, cor1, cor2):
        self.tam = tam
        self.cor1 = cor1
        self.cor2  = cor2
        self.casas_matriz = []
        self.casas_dispo = []
        self.matriz_pos = []
        self.tam_casa = None
        self.prox_jogada = 1
        self.modo = "select"
        self.casa_atual = None
        self.ajust_tam()
        self.create_casas()
        self.click = False
        self.peca_kill = None

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

        #criando as pecas do player 2
        for i in range(5,8):
            for j in range(8):
                if self.casas_matriz[i][j].color == self.cor1:
                    peca = Peca(self.matriz_pos[i][j]["x"],self.matriz_pos[i][j]["y"],self.tam_casa/2 - (self.tam_casa/6),(255,255,255),1)
                    peca.player = 2
                    self.casas_matriz[i][j].set_ocupado(peca)
                    self.casas_matriz[i][j].player = 2

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

    def atualizar_matriz_casas_reset(self, i, j, casa):
        self.casas_matriz[i][j] = casa

    def casa_select(self, i, j):
        self.casas_matriz[i][j].color = "yellow"
        self.casas_matriz[i][j].select = True

    def remove_peca_kill(self):
        if self.peca_kill is not None and self.peca_kill.ocupado is not None:
            self.peca_kill.ocupado = None
            self.casas_matriz[self.peca_kill.i][self.peca_kill.j] = self.peca_kill

    def realizar_jogada(self, casa):
        self.casa_atual.ocupado.posX = self.matriz_pos[casa.i][casa.j]["x"]
        self.casa_atual.ocupado.posY = self.matriz_pos[casa.i][casa.j]["y"]
        casa.ocupado = self.casa_atual.ocupado
        casa.player = self.prox_jogada
        self.casa_atual.ocupado = None
        self.atualizar_matriz_casas(self.casa_atual.i,self.casa_atual.j)
        casa.disponivel = False
        self.set_prox_jogada()
        self.reset()
        self.remove_peca_kill()
        load_music('./assets/movimento.mp3')
        pygame.mixer.music.play()
        #pygame.mixer.music.play()

    def check_click(self, pos):
        i, j = self.get_casa_click(pos)
        casa = self.casas_matriz[i][j]

        if casa.ocupado is not None and casa.player == self.prox_jogada:
            if self.casa_atual is not None:
                self.reset()
            self.casa_atual = casa
            self.casa_select(i,j)
            detalhe = {
                "activate": False,
                "direction": None,
            }
            self.show_jogadas(casa, detalhe)
        elif casa.disponivel:
            self.realizar_jogada(casa)
             
    def activate_disponivel(self, i,j):
        self.casas_matriz[i][j].color = "yellow"
        self.casas_matriz[i][j].disponivel = True
        self.casas_dispo.append(self.casas_matriz[i][j])

    def show_jogadas(self, casa, detalhes):
        if self.prox_jogada == 1:
            chave = 1
        else:
            chave = -1
        print(f'chave {chave} - {detalhes}')
        
        if detalhes["activate"]:
            if detalhes["direction"] == "right":
                if casa.j+1 < 7:
                    if self.casas_matriz[casa.i+1*chave][casa.j+1].ocupado == None:
                        self.activate_disponivel(casa.i+(1*chave),casa.j+1)
                        self.peca_kill = casa
            else:
                if casa.j-1 > 0:
                    if self.casas_matriz[casa.i+1*chave][casa.j-1].ocupado == None:
                        self.activate_disponivel(casa.i+(1*chave),casa.j-1)
                        self.peca_kill = casa

        else:
            #primeira possibilidade: 1 caminho para a esquerda
            if casa.j+1 > 7:
                print("caminho 1")
                if self.casas_matriz[casa.i+(1*chave)][casa.j-1].ocupado is not None:
                    if self.casas_matriz[casa.i+(1*chave)][casa.j-1].player != self.prox_jogada:
                        detalhe = {
                            "activate": True,
                            "direction": "left",
                        }
                        self.show_jogadas(self.casas_matriz[casa.i+(1*chave)][casa.j-1], detalhe)
                else:
                    self.activate_disponivel(casa.i+1*chave,casa.j-1)
            #segunda possibilidade: 1 caminho para a direita
            elif casa.j-1 < 0:
                print("caminho 2")
                if self.casas_matriz[casa.i+(1*chave)][casa.j+1].ocupado is not None:
                    if self.casas_matriz[casa.i+(1*chave)][casa.j+1].player != self.prox_jogada:
                        detalhe = {
                            "activate": True,
                            "direction": "right",
                        }
                        self.show_jogadas(self.casas_matriz[casa.i+(1*chave)][casa.j+1], detalhe)
                else:
                    self.activate_disponivel(casa.i+(1*chave),casa.j+1)
            #terceira possibilidade: 2 caminhos (direita e esquerda)
            else:
                print("caminho 3")
                if self.casas_matriz[casa.i+(1*chave)][casa.j+1].ocupado is not None:
                    if self.casas_matriz[casa.i+(1*chave)][casa.j+1].player != self.prox_jogada:
                        detalhe = {
                            "activate": True,
                            "direction": "right",
                    }
                        self.show_jogadas(self.casas_matriz[casa.i+(1*chave)][casa.j+1], detalhe)
                else:
                    self.activate_disponivel(casa.i+(1*chave),casa.j+1)

                if self.casas_matriz[casa.i+(1*chave)][casa.j-1].ocupado is not None:
                    if self.casas_matriz[casa.i+(1*chave)][casa.j-1].player != self.prox_jogada:
                        detalhe = {
                            "activate": True,
                            "direction": "left",
                        }
                        self.show_jogadas(self.casas_matriz[casa.i+(1*chave)][casa.j-1], detalhe)
                else:
                    self.activate_disponivel(casa.i+(1*chave),casa.j-1)
                
                    
    def reset(self):
        self.casa_atual.color = self.cor1
        for casa in self.casas_dispo:
            casa.color = self.cor1
            casa.disponivel = False
            self.atualizar_matriz_casas_reset(casa.i,casa.j,casa)

    def check_kill(self):
        return True
    
    def print_infos(self):
        for i in range(8):
            for j in range(8):
                print(self.casas_matriz[i][j])
        