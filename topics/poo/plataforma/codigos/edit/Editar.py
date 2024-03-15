from cenario.Ground import GroundUnique
import pygame

class Editar:
    def __init__(self) -> None:
        self.matriz = []
        self.linhas = 22
        self.colunas = 40
        self.montar_matriz()
       
    def montar_matriz(self):
        for linhas in range(self.linhas):
            linha = []
            for colunas in range(self.colunas):
                linha.append(0)
            self.matriz.append(linha)

        for i in self.matriz:
            print(i)

    def show(self, screen):
        #linhas horizontais
        for i in range(self.linhas):
            for j in range(self.colunas):
                pygame.draw.line(screen,(200,200,200),(j*32,0),(j*32,720))
                pygame.draw.line(screen,(200,200,200),(0,i*32),(1280,i*32))
        #linhas verticais
    
    def get_ij_click(self, pos):
        i = int(pos[1]/32)
        j = int(pos[0]/32)
        return (i,j)
    
    def criar_elemento(self, i, j):
        self.matriz[i][j] = 1
    
