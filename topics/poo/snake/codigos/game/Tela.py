import pygame

from game.Button import ButtonRestart,ButtonPause, ButtonInit

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
        button_pause = ButtonPause("blue", "white",1040,300,"pause",self.screen,"./assets/fonts/Potato_sans-Black.otf")
        button_init = ButtonInit("green", "white",1040,400,"iniciar",self.screen,"./assets/fonts/Potato_sans-Black.otf")
        self.buttons.append(button_pause)
        self.buttons.append(button_restart)
        self.buttons.append(button_init)

    def show(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        for button in self.buttons:
            button.show()

    def write(self, texto, x,y, color):
        texto_superficie = self.fonte.render(texto, True, color)
        self.screen.blit(texto_superficie, (x,y))

    def check_click(self,x, y):
        pygame.time.wait(150)
        dados = []
        for button in self.buttons:
            if button.check_click(x,y):
                if button.active:
                        dados.append({
                                "function": button.function,
                                "status": button.active,
                        })
        return dados 
            

    

    



    