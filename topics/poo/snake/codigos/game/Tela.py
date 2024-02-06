import pygame

from game.Button import ButtonRestart,ButtonPause, ButtonInit
from game.Bosters import Imagem

class Tela:
    def __init__(self, screen, tam_fonte) -> None:
        self.screen = screen
        self.fonte = pygame.font.Font("./assets/fonts/Browood-Regular.ttf", tam_fonte)  
        self.width = 250
        self.heigth = 700
        self.color = (200,200,200)
        self.rect = pygame.Rect(1020,10,self.width, self.heigth)
        self.buttons = []
        self.imgs = []
        self.show()

    def set_tam_font(self, tam_fonte):
        self.fonte = pygame.font.Font("./assets/fonts/Browood-Regular.ttf", tam_fonte) 

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
    
    def load_img(self, url_img, x, y, width, height):
        img = Imagem(url_img,x,y,width, height)
        self.imgs.append(img)

class TelaInfos(Tela):
    def __init__(self, screen, fonte) -> None:
        super().__init__(screen, fonte)
        self.color = (0,0,255)
        self.create_buttons()
        self.modelife3()

    def modelife3(self):
        self.imgs = []
        self.load_img("./assets/Graphics/coracao.png", 1040,250,60,60)
        self.load_img("./assets/Graphics/coracao.png", 1120,250,60,60)
        self.load_img("./assets/Graphics/coracao.png", 1200,250,60,60)

    def modelife2(self):
        self.imgs.pop(len(self.imgs)-1)
        self.load_img("./assets/Graphics/coracao_black.png", 1200,250,60,60)

    def modelife1(self):
        self.imgs.pop(len(self.imgs)-2)
        self.load_img("./assets/Graphics/coracao_black.png", 1120,250,60,60)

    def show_imgs(self):
        for img in self.imgs:
            img.show(self.screen)

    def create_buttons(self):
        pass
        #button_restart = ButtonRestart("black","red",1040,500,"restart", self.screen, "./assets/fonts/Potato_sans-Black.otf")
        #self.buttons.append(button_restart)
        

class TelaGameOver(Tela):
    def __init__(self, screen, tam_fonte) -> None:
        super().__init__(screen, tam_fonte)
        self.width = 1260
        self.heigth = 700
        self.color = (255,0,0)
        self.rect = pygame.Rect(10,10,self.width, self.heigth)
        self.create_buttons()

    def create_buttons(self):
        button_restart = ButtonRestart("blue","white",530,350,"restart", self.screen, "./assets/fonts/Potato_sans-Black.otf")
        self.buttons.append(button_restart) 

class TelaInicio(Tela):
    def __init__(self, screen, tam_fonte) -> None:
        super().__init__(screen, tam_fonte)
        self.width = 1260
        self.heigth = 700
        self.color = (0,255,0)
        self.rect = pygame.Rect(10,10,self.width, self.heigth)
        self.create_buttons()

    def create_buttons(self):
        button_init = ButtonInit("blue","white",530,350,"start", self.screen, "./assets/fonts/Potato_sans-Black.otf")
        self.buttons.append(button_init) 

    

    



    