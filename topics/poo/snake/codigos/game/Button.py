import pygame

def load_music(caminho):
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

class Button:
    def __init__(self, cor1, cor2, x, y, text, screen, font_file) -> None:
        self.cor1 = cor1
        self.cor2 = cor2
        self.x = x
        self.y = y
        self.active = False
        self.text = text
        self.width_text = len(self.text)*15
        self.width = 100+self.width_text
        self.height = 50
        self.rect = pygame.Rect(self.x,self.y,self.width, self.height)
        self.screen = screen
        self.fonte = pygame.font.Font(font_file,self.height-20)

    def show(self):
        pygame.draw.rect(self.screen,self.cor1,self.rect,0,20)
        texto_superficie = self.fonte.render(self.text, True, self.cor2)
        self.screen.blit(texto_superficie, (self.x+45,self.y+10))

    def check_click(self, x, y):
        if x >= self.x and x <= self.x+self.width and y <= self.y+self.height and y >= self.y:
            self.action()
            load_music("./assets/musics/button.mp3")
            return True
        else:
            return False
    
    def action(self):
        self.active = True
        
class ButtonRestart(Button):
    def __init__(self, cor1, cor2, x, y, text, screen, font_file) -> None:
        super().__init__(cor1, cor2, x, y, text, screen, font_file)
        self.function = "restart"

class ButtonInit(Button):
    def __init__(self, cor1, cor2, x, y, text, screen, font_file) -> None:
        super().__init__(cor1, cor2, x, y, text, screen, font_file)
        self.function = "start"