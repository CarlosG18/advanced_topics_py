import pygame

class Element:
    def __init__(self, url_img, x, y):
        self.url_img = url_img
        self.width = 50
        self.height = 50
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

class Head(Element):
    def __init__(self, x, y) -> None:
        return super().__init__("./assets/Graphics/head_left.png", x, y)

class Body(Element):
    def __init__(self, x, y) -> None:
        return super().__init__("./assets/Graphics/body_horizontal.png", x, y)

class Tail(Element):
    def __init__(self, x, y) -> None:
        return super().__init__("./assets/Graphics/tail_right.png", x, y)
    