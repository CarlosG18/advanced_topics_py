import pygame
from pygame.sprite import Group

class Animation(pygame.sprite.Sprite):
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

