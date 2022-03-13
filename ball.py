import pygame

# class Ball
class Ball:
    def __init__(self, window):
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.window = window
        self.window_rect = self.window.get_rect()
        self.rect.centerx = self.window.get_width() / 2
        self.rect.centery = self.window.get_height() / 2

    def draw(self):
        self.window.blit(self.image, self.rect)