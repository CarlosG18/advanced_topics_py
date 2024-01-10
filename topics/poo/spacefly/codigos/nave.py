import pygame

class Nave(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (1280/2, 720/2)

    def move_left(self):
        self.rect.x -= 5
    
    def move_right(self):
        self.rect.x += 5

    def move_up(self):
        self.rect.y -= 5

    def move_down(self):
        self.rect.y += 5
    