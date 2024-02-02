import pygame

from game.Button import ButtonRestart

class Tela:
    def __init__(self, screen, fonte) -> None:
        self.screen = screen
        self.fonte = fonte
        self.width = 250
        self.heigth = 700
        self.color = (200,200,200)
        self.rect = pygame.Rect(1020,10,self.width, self.heigth)
        self.buttons = []
        self.show()
        self.create_buttons()

    def create_buttons(self):
        button_restart = ButtonRestart("black","red",1040,500,"restart", self.screen, "./assets/fonts/Potato_sans-Black.otf")
        self.buttons.append(button_restart)

    def show(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        for button in self.buttons:
            button.show()

    def write(self, texto, x,y, color):
        texto_superficie = self.fonte.render(texto, True, color)
        self.screen.blit(texto_superficie, (x,y))

    def check_click(self,x, y):
        for button in self.buttons:
            if button.check_click(x,y):
                button.action()
            

    

    



    