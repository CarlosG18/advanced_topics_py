import pygame
from pygame.sprite import Group

class GroundElement(pygame.sprite.Sprite):
    def __init__(self, img) -> None:
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.width = 32
        self.height = 32

class GroundTopLeft(GroundElement):
    def __init__(self) -> None:
        super().__init__("./assets/cenario/tiles/Tile_01.png")

class GroundTopRight(GroundElement):
    def __init__(self) -> None:
        super().__init__("./assets/cenario/tiles/Tile_04.png")

class GroundTop(GroundElement):
    def __init__(self) -> None:
        super().__init__("./assets/cenario/tiles/Tile_02.png")

class GroundCenter(GroundElement):
    def __init__(self) -> None:
        super().__init__("./assets/cenario/tiles/Tile_12.png")

class GroundDownLeft(GroundElement):
    def __init__(self) -> None:
        super().__init__("./assets/cenario/tiles/Tile_19.png")

class GroundDownRight(GroundElement):
    def __init__(self) -> None:
        super().__init__("./assets/cenario/tiles/Tile_22.png")

class GroundLeft(GroundElement):
    def __init__(self) -> None:
        super().__init__("./assets/cenario/tiles/Tile_10.png")

class GroundRight(GroundElement):
    def __init__(self) -> None:
        super().__init__("./assets/cenario/tiles/Tile_13.png")

class GroundDown(GroundElement):
    def __init__(self) -> None:
        super().__init__("./assets/cenario/tiles/Tile_21.png")

class ConjuntoGround(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.group_conjunto = Group()
        self.create()

    def create(self):
        #top left
        top_left = GroundTopLeft()
        top_left.rect.x = self.pos_x
        top_left.rect.y = self.pos_y
        self.group_conjunto.add(top_left)

        #top
        for i in range(self.width):
            top = GroundTop()
            top.rect.x = (self.pos_x + top.width) + (i * top.width)
            top.rect.y = self.pos_y
            self.group_conjunto.add(top)

        #top right
        top_right = GroundTopRight()
        top_right.rect.x = (self.pos_x + top.width) + (self.width * top.width)
        top_right.rect.y = self.pos_y
        self.group_conjunto.add(top_right)
        
        #left
        for j in range(self.height):
            left = GroundLeft()
            left.rect.y = (self.pos_y + left.height) + (j * left.height)
            left.rect.x = self.pos_x
            self.group_conjunto.add(left)
        
        #right
        for j in range(self.height):
            right = GroundRight()
            right.rect.y = (self.pos_y + right.height) + (j * right.height)
            right.rect.x = (self.pos_x + right.width) + (self.width * right.width)
            self.group_conjunto.add(right)
        
        #downleft 
        down_left = GroundDownLeft()
        down_left.rect.y = (self.pos_y + down_left.height) + (self.height * down_left.height)
        down_left.rect.x = self.pos_x
        self.group_conjunto.add(down_left)

        #downright
        down_right = GroundDownRight()
        down_right.rect.y = (self.pos_y + down_right.height) + (self.height * down_right.height)
        down_right.rect.x = (self.pos_x + down_right.width) + (self.width * down_right.width)
        self.group_conjunto.add(down_right)

        #down
        for i in range(self.width):
            down = GroundDown()
            down.rect.x = (self.pos_x + down.width) + (i * down.width)
            down.rect.y = (self.pos_y + down.height) + (self.height * down.height)
            self.group_conjunto.add(down)

        #center
        for i in range(self.width):
            for j in range(self.height):
                center = GroundCenter()
                center.rect.x = (self.pos_x + center.width) + (i * center.width)
                center.rect.y = (self.pos_y + center.height) + (j* center.height)
                self.group_conjunto.add(center)

    def show(self, screen):
        self.group_conjunto.draw(screen)
                
        
                
        


    