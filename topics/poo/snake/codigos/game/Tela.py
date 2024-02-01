import pygame

class Button:
    def __init__(self, cor1, cor2, x, y, width, height, text, screen, fonte) -> None:
        self.cor1 = cor1
        self.cor2 = cor2
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.rect = pygame.Rect(self.x,self.y,self.width, self.height)
        self.screen = screen
        self.fonte = fonte

    def show(self):
        pygame.draw.rect(self.screen,self.cor1,self.rect)
        texto_superficie = self.fonte.render(self.text, True, self.cor2)
        self.screen.blit(texto_superficie, (self.x+(self.width/2),self.y+(self.height/2)))

class Tela:
    def __init__(self, screen, fonte) -> None:
        self.screen = screen
        self.fonte = fonte
        self.width = 250
        self.heigth = 700
        self.color = (200,200,200)
        self.rect = pygame.Rect(1020,10,self.width, self.heigth)
        self.button_restart = Button("red","black",1040,500,200,100,"restart", screen, fonte)
        self.show()

    def show(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        self.button_restart.show()

    def write(self, texto, x,y, color):
        texto_superficie = self.fonte.render(texto, True, color)
        self.screen.blit(texto_superficie, (x,y))



    