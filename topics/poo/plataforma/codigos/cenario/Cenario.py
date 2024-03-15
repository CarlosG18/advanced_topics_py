import pygame
from pygame.sprite import Group
from cenario.Ground import ConjuntoGround, ConjuntoGroundUnique

#matriz_fase com 40 colunas e 22 linhas, 0 para vazio e 1 para elemento de ground

class Cenario:
    def __init__(self, matriz_fase, personagem) -> None:
        self.matriz = matriz_fase
        self.gravity = True
        self.personagem = personagem
        self.groups_cenario = []
        self.colisao = None
        self.list_colisoes = [None,None]
        #self.create()

    def update_matriz(self, matriz):
        self.matriz = matriz
        if self.groups_cenario != []:
            self.groups_cenario.clear()
        blocos = ConjuntoGroundUnique(self.matriz)
        self.groups_cenario.append(blocos)


    def create(self):
        bloco1 = ConjuntoGround(10,2,0,500)
        bloco2 = ConjuntoGround(30,2,200,100)
        blocos = ConjuntoGroundUnique(self.matriz)
        self.groups_cenario.append(bloco1)
        self.groups_cenario.append(bloco2)
        self.groups_cenario.append(blocos)

    def show(self, screen):
        #self.check_colisao()
        if self.gravity:
            self.gravidade()
        else:
            self.stop_gravidade()
        for elemento in self.groups_cenario:
            elemento.show(screen)

    def gravidade(self):
        if self.gravity:
            self.personagem.personagem.rect.y += 5
            self.personagem.att_pos()

    def stop_gravidade(self):
        self.gravity = False
    
    def set_gravidade(self):
        self.gravity = True

    def check_colisao(self):
        #adicionando as listas de colisoes
        for index,bloco in enumerate(self.groups_cenario):
            self.list_colisoes[index] = pygame.sprite.groupcollide(self.personagem.personagem_animate,bloco.group_conjunto, False, False)
           
        if self.list_colisoes[0] or self.list_colisoes[1]:
            self.stop_gravidade()
        else:
            self.set_gravidade()
        