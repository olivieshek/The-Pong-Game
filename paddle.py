import pygame

# wo
class Paddle:
    def __init__(self, window, x_pos, objImage):
        self.image = objImage
        self.rect = self.image.get_rect()
        self.window = window
        self.window_rect = self.window.get_rect()
        self.rect.centerx = x_pos
        self.rect.centery = self.window.get_height() / 2
        self.speed = 20

    def draw(self):
        self.window.blit(self.image, self.rect)