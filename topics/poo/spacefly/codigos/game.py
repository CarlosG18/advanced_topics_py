import pygame
from nave import Nave

class Game:
    def __init__(self) -> None:
        self.sprites_nave = pygame.sprite.Group()
        self.nave_principal = Nave()
        self.sprites_nave.add(self.nave_principal)

    def move_nave_principal(self, key):
        if key[pygame.K_UP]:
            self.nave_principal.move_up()
        elif key[pygame.K_DOWN]:
            self.nave_principal.move_down()
        elif key[pygame.K_LEFT]:
            self.nave_principal.move_left()
        elif key[pygame.K_RIGHT]:
            self.nave_principal.move_right()
        
            
    def upgrade(self, screen):
        self.sprites_nave.update()
        self.sprites_nave.draw(screen)

    def tela_inicial(self):
        pass
