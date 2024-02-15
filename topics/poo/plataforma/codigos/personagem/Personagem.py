import pygame
from pygame.sprite import Group

class Animacao(pygame.sprite.Sprite):
    def __init__(self, img_sprites, width_frame, height_frame) -> None:
        super().__init__()
        self.frames = self.get_frames_from_img(img_sprites, width_frame, height_frame)
        self.frame_atual = 0
        self.image = self.frames[self.frame_atual]
        self.rect = self.image.get_rect()

    def get_frames_from_img(self, img_sprites, width_frame, height_frame):
        frames = []
        img_frames = pygame.image.load(img_sprites)
        img_width, img_height = img_frames.get_size()

        for y in range(0, img_height, height_frame):
            for x in range(0, img_width, width_frame):
                frame = img_frames.subsurface(pygame.Rect(x,y,width_frame, height_frame))
                frames.append(frame)
        return frames

    def update(self):
        self.frame_atual = (self.frame_atual + 1) % len(self.frames)
        self.image = self.frames[self.frame_atual]
    
    def troca_animacao(self, img_sprites, width_frame, height_frame):
        self.__init__(img_sprites, width_frame, height_frame)

class Personagem:
    def __init__(self) -> None:
        self.personagem = Animacao("./assets/graphics/3/Walk.png",96,96)
        self.personagem_animate = Group(self.personagem)
        self.pos_x = self.personagem.rect.x
        self.pos_y = self.personagem.rect.y
        self.animacao_atual = "walk"
        self.troca_animacao = False

    def show(self, screen): 
        self.personagem_animate.draw(screen)
        self.att_pos()

    def att_pos(self):
        self.pos_x = self.personagem.rect.x
        self.pos_y = self.personagem.rect.y

    def redefinir_pos(self):
        self.personagem.rect.x = self.pos_x
        self.personagem.rect.y = self.pos_y


    def walk(self, direction):
        if self.animacao_atual != "walk":
            self.troca_animacao = True
        self.animacao_atual = "walk"
        self.check_animate()
        if direction == "left":
            self.personagem.rect.x -= 5
            self.att_pos()
        elif direction == "right":
            self.personagem.rect.x += 5
            self.att_pos()
        self.personagem_animate.update() 
    
    def check_animate(self):
        if self.troca_animacao:
            if self.animacao_atual == "fly":
                self.personagem.troca_animacao("./assets/graphics/3/Special.png",96,96)
            elif self.animacao_atual == "walk":
                self.personagem.troca_animacao("./assets/graphics/3/Walk.png",96,96)
        self.redefinir_pos()
        self.troca_animacao = False

    def fly(self):
        if self.animacao_atual != "fly":
            self.troca_animacao = True
        self.animacao_atual = "fly"
        self.check_animate()
        self.personagem.rect.y -= 10
        self.personagem_animate.update() 
