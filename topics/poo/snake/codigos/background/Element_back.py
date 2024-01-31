import pygame

class Element_Back:
    def __init__(self, i, j, x, y, color) -> None:
        self.i = i
        self.j = j
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.color = color
        self.react = pygame.Rect(self.x, self.y, self.width, self.height)

    def show(self, screen):
        pygame.draw.rect(screen,self.color,self.react)

    def __str__(self):
        return f'elemento[{self.i}][{self.j}]. x={self.x}, y={self.y}'

    
