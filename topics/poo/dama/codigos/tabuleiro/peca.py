import pygame

class Peca:
    def __init__(self, posX, posY, raio, cor, player):
        self.posX = posX
        self.posY = posY
        self.raio = raio
        self.cor = cor
        self.player = player

    def show(self, screen):
        self.peca = pygame.Vector2(self.posX, self.posY)
        pygame.draw.circle(screen, self.cor, self.peca, self.raio)

    def __str__(self):
        return f'peca do player {self.player} da cor {self.cor}'
    
