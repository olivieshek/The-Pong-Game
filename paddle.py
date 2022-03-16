from curses import KEY_UP
import pygame

class Paddle:
    def __init__(
        self,
        window,
        isAuto=False,
        color=(255, 255, 255),
        key_up=pygame.K_UP,
        key_down=pygame.K_DOWN,
        velocity=10
    ):
        self.image = pygame.Surface((10, 100))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.window = window
        self.window_rect = self.window.get_rect()
        if isAuto is True:
            self.rect.centerx = window.get_width() - window.get_width() / 30 - self.image.get_width() / 2
        else:
            self.rect.centerx = window.get_width() / 30 + self.image.get_width() / 2
        self.rect.centery = self.window.get_height() / 2
        # if isAuto == True:
        #     print('auto')
        self.key_up = key_up
        self.key_down = key_down
        self.velocity = velocity
        self.isAuto = isAuto

    def draw(self):
        self.window.blit(self.image, self.rect)

    def controls(self, keys):
        if self.isAuto:
            pass
        else:
            if keys[self.key_up]:
                self.rect.y -= self.velocity
            if keys[self.key_down]:
                self.rect.y += self.velocity