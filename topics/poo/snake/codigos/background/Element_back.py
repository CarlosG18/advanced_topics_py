import pygame

class Element_Back:
    def __init__(self, i, j, top, left, color) -> None:
        self.i = i
        self.j = j
        self.width = 50
        self.height = 50
        self.x = top
        self.y = left
        self.color = color
        self.react = pygame.Rect(self.y, self.x, self.width, self.height)

    def show(self, screen):
        pygame.draw.rect(screen,self.color,self.react)

    def __str__(self):
        return f'elemento[{self.i}][{self.j}]. x={self.x}, y={self.y}'