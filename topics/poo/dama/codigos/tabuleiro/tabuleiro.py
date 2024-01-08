import pygame
from .casa import Casa
from .peca import Peca

def load_music(caminho):
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

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
        self.tag_kill = False
        self.tag_jogada = False
        self.priority = []
        self.modo_dama = []

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
                self.casas_matriz[i][j].create(screen)
                if self.casas_matriz[i][j].ocupado is not None:
                    self.casas_matriz[i][j].ocupado.show(screen)

    def get_casa_click(self, pos):
        col = int(pos[0]/self.tam_casa)
        row = int(pos[1]/self.tam_casa)
        return (row, col)
        
    def atualizar_matriz_casas(self, i, j, casa):
        self.casas_matriz[i][j] = casa

    def atualizar_casa_atual(self):
        self.casas_matriz[self.casa_atual.i][self.casa_atual.j] = self.casa_atual

    def casa_select(self, i, j):
        self.casas_matriz[i][j].color = "yellow"
        self.casas_matriz[i][j].select = True

    def casa_deselect(self):
        self.casa_atual.color = self.cor1
        self.casa_atual.select = False

    def remove_peca_kill(self):
        if self.peca_kill is not None and self.peca_kill.ocupado is not None:
            self.peca_kill.ocupado = None
            self.peca_kill.player = None
            self.casas_matriz[self.peca_kill.i][self.peca_kill.j] = self.peca_kill
        self.peca_kill = None
        load_music('./assets/ze.mp3')

    def realizar_jogada(self, casa):
        #alterando a posição da peça para a casa disponivel selecionada
        self.casa_atual.ocupado.posX = self.matriz_pos[casa.i][casa.j]["x"]
        self.casa_atual.ocupado.posY = self.matriz_pos[casa.i][casa.j]["y"]
        #fazendo as atribuições para a nova casa
        casa.ocupado = self.casa_atual.ocupado
        casa.player = self.prox_jogada
        self.casa_atual.ocupado = None
        self.casa_atual.player = None
        self.atualizar_matriz_casas(casa.i,casa.j,casa)
        #limpando as casa disponiveis e a casa selecionada
        self.clear_disponivel()
        self.casa_deselect()
        #atualizando a matriz de casas (porque a casa atual foi alterada)
        self.atualizar_casa_atual()
        self.casa_atual = None
        #executar o som de movimento
        load_music('./assets/movimento.mp3')

    def clear_disponivel(self):
        for casa in self.casas_dispo:
            casa.disponivel = False
            casa.color = self.cor1
            self.atualizar_matriz_casas(casa.i,casa.j,casa)
        self.casas_dispo = []

    def check_priority(self, player):
        self.priority = []
        for i in range(8):
            for j in range(8):
                if self.casas_matriz[i][j].player == player:
                    resposta = self.check_kill(self.casas_matriz[i][j])
                    if resposta["kill"]:
                        self.priority.append(self.casas_matriz[i][j])

    def check_kill(self, casa):
        detalhes = {
            "kill": False,
            "directions": [],
            "kill_peca": None,
        }
    
        if casa.i - 2 >= 0:
            if casa.j - 2 >=0:
                #verificando o canto superior esquerdo   
                if not self.casa_is_none(casa.i-1,casa.j-1) and not self.casa_is_player(casa.i-1,casa.j-1):
                    if self.casa_is_none(casa.i-2,casa.j-2):
                        detalhes["kill"] = True
                        infos = {
                            "i": int(casa.i-2),
                            "j": int(casa.j-2),
                        }
                        detalhes["directions"].append(infos)
                        infos_kill_peca = {
                            "i": int(casa.i-1),
                            "j": int(casa.j-1),
                        }
                        detalhes["kill_peca"] = infos_kill_peca
            if casa.j + 2 < 8:
                #verificado o canto superior direito
                if not self.casa_is_none(casa.i-1,casa.j+1) and not self.casa_is_player(casa.i-1,casa.j+1):
                    if self.casa_is_none(casa.i-2,casa.j+2):
                        detalhes["kill"] = True
                        infos = {
                            "i": int(casa.i-2),
                            "j": int(casa.j+2),
                        }
                        detalhes["directions"].append(infos)
                        infos_kill_peca = {
                            "i": int(casa.i-1),
                            "j": int(casa.j+1),
                        }
                        detalhes["kill_peca"] = infos_kill_peca
        if casa.i + 2 < 8:
            if casa.j - 2 >=0:
                #verificando o canto inferior esquerdo   
                if not self.casa_is_none(casa.i+1,casa.j-1) and not self.casa_is_player(casa.i+1,casa.j-1):
                    if self.casa_is_none(casa.i+2,casa.j-2):
                        detalhes["kill"] = True
                        infos = {
                            "i": int(casa.i+2),
                            "j": int(casa.j-2),
                        }
                        detalhes["directions"].append(infos)
                        infos_kill_peca = {
                            "i": int(casa.i+1),
                            "j": int(casa.j-1),
                        }
                        detalhes["kill_peca"] = infos_kill_peca
            if casa.j + 2 < 8:
                #verificado o canto inferior direito
                if not self.casa_is_none(casa.i+1,casa.j+1) and not self.casa_is_player(casa.i+1,casa.j+1):
                    if self.casa_is_none(casa.i+2,casa.j+2):
                        detalhes["kill"] = True
                        infos = {
                            "i": int(casa.i+2),
                            "j": int(casa.j+2),
                        }
                        detalhes["directions"].append(infos)
                        infos_kill_peca = {
                            "i": int(casa.i+1),
                            "j": int(casa.j+1),
                        }
                        detalhes["kill_peca"] = infos_kill_peca
        return detalhes

    def click_on(self, casa):
        if self.casa_atual is not None:
            self.casa_deselect()
            self.clear_disponivel()
        self.casa_atual = casa
        self.casa_select(casa.i,casa.j)
        self.show_jogadas(casa)

    def check_continue_player(self,casa):
        resp = self.check_kill(casa)
        if resp["kill"] and self.tag_kill:
            self.casa_atual = casa
            self.show_jogadas(casa)
        else:
            self.tag_kill = False
            self.set_prox_jogada()
    
    def check_click(self, pos):
        i, j = self.get_casa_click(pos)
        casa = self.casas_matriz[i][j]

        if not self.casa_is_none(i,j) and casa.player == self.prox_jogada:
            if not (self.priority == []):
                for casa_p in self.priority:
                    if casa.i == casa_p.i and casa.j == casa_p.j:
                        self.click_on(casa)
            else:
                self.click_on(casa)
        elif casa.disponivel:
            self.realizar_jogada(casa)
            if self.tag_kill:
                self.remove_peca_kill()
            self.check_continue_player(casa)
            self.check_priority(self.prox_jogada)
             
    def activate_disponivel(self, i,j):
        self.casas_matriz[i][j].color = "yellow"
        self.casas_matriz[i][j].disponivel = True
        self.casas_dispo.append(self.casas_matriz[i][j])

    def show_jogadas(self, casa):
        #define se é player 1 (chave = 1) ou player 2 (chave = -1)
        if self.prox_jogada == 1:
            chave = 1
        else:
            chave = -1
        
        #primeira possibilidade: 1 caminho para a esquerda
        if casa.j+1 > 7:
            if not self.casa_is_none(casa.i+(1*chave),casa.j-1):
                if not self.casa_is_player(casa.i+(1*chave),casa.j-1):
                    detalhes = self.check_kill(casa)
                    if detalhes["kill"]:
                        self.tag_kill = True
                        self.peca_kill = self.casas_matriz[detalhes["kill_peca"]["i"]][detalhes["kill_peca"]["j"]]
                        for direcao in detalhes["directions"]:
                            i = direcao["i"]
                            j = direcao["j"]
                            self.activate_disponivel(i,j)
            else:
                self.activate_disponivel(casa.i+1*chave,casa.j-1)
        #segunda possibilidade: 1 caminho para a direita
        elif casa.j-1 < 0:
            if not self.casa_is_none(casa.i+(1*chave),casa.j+1):
                if not self.casa_is_player(casa.i+(1*chave),casa.j+1):
                    detalhes = self.check_kill(casa)
                    if detalhes["kill"]:
                        self.tag_kill = True
                        self.peca_kill = self.casas_matriz[detalhes["kill_peca"]["i"]][detalhes["kill_peca"]["j"]]
                        for direcao in detalhes["directions"]:
                            i = direcao["i"]
                            j = direcao["j"]
                            self.activate_disponivel(i,j)
            else:
                self.activate_disponivel(casa.i+(1*chave),casa.j+1)
        #terceira possibilidade: 2 caminhos (direita e esquerda)
        else:
            right, left = self.casas_prox_none(casa,chave)
            detalhes = self.check_kill(casa)

            if detalhes["kill"]:
                self.tag_kill = True
                self.peca_kill = self.casas_matriz[detalhes["kill_peca"]["i"]][detalhes["kill_peca"]["j"]]
                for direcao in detalhes["directions"]:
                    i = direcao["i"]
                    j = direcao["j"]
                    self.activate_disponivel(i,j)
            else:    
                if not self.tag_kill and right:
                    self.activate_disponivel(casa.i+(1*chave),casa.j+1)

                if not self.tag_kill and left:
                    self.activate_disponivel(casa.i+(1*chave),casa.j-1)
        
    def show_jogadas_continue(self):
        pass
        
    def casa_is_none(self, i,j):
        if self.casas_matriz[i][j].ocupado == None:
            return True
        else:
            return False
        
    def casa_is_player(self, i, j):
        if self.casas_matriz[i][j].player == self.prox_jogada:
            return True
        else:
            return False
                    
    def casas_prox_none(self, casa, chave):
        right = False
        left = False
        if chave == 1:
            if not casa.i + 1 >= 8:
                if self.casa_is_none(casa.i+(1*chave),casa.j+1):
                    right = True
                if self.casa_is_none(casa.i+(1*chave),casa.j-1):
                    left = True
        else:
            if not casa.i - 1 < 0:
                if self.casa_is_none(casa.i+(1*chave),casa.j+1):
                    right = True
                if self.casa_is_none(casa.i+(1*chave),casa.j-1):
                    left = True

        return (right, left)