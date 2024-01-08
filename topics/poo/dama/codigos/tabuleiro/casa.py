import pygame

class Casa:
    def __init__(self,i,j, x, y, width, height, color):
        self.i = i
        self.j = j
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.ocupado = None
        self.disponivel = False
        self.select = False
        self.color = color
        self.player = None

    def create(self, screen):
        self.casa = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen,self.color,self.casa)
        
    def set_ocupado(self, peca):
        self.ocupado = peca

    def __str__(self):
        return f'casa[{self.i}][{self.j}]'