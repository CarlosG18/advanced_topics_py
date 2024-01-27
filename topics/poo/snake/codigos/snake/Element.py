import pygame

class Element:
    def __init__(self, url_img, x, y, i, j):
        self.url_img = url_img
        self.width = 50
        self.height = 50
        self.i = i
        self.j = j
        self.x = x
        self.y = y
        self.element = pygame.image.load(self.url_img)
        self.element_rect = None
        self.create()

    def create(self):
        self.element = pygame.transform.scale(self.element, (self.width,self.height))
        self.element_rect = self.element.get_rect()
        self.element_rect.x = self.x
        self.element_rect.y = self.y

    def show(self, screen):
        screen.blit(self.element, self.element_rect)

    def troca_img_element(self, url_img):
        self.url_img = url_img
        self.element = pygame.image.load(self.url_img)
    
    def update_pos(self, matriz):
        self.x = matriz[self.i][self.j]["x"]
        self.y = matriz[self.i][self.j]["y"]
        self.element_rect.x = self.x
        self.element_rect.y = self.y

class Head(Element):
    def __init__(self, x, y, i, j) -> None:
        return super().__init__("./assets/Graphics/head_left.png", x, y, i, j)

class Body(Element):
    def __init__(self, x, y, i, j) -> None:
        return super().__init__("./assets/Graphics/body_horizontal.png", x, y, i, j)

class Tail(Element):
    def __init__(self, x, y, i, j) -> None:
        return super().__init__("./assets/Graphics/tail_right.png", x, y, i, j)
    