import pygame

pygame.font.init()
myFont = pygame.font.SysFont('Arial', 30)


class Score:
    def __init__(
        self,
        window,
        pos_x=0,
        pos_y=0,
        color=(255, 255, 255),
        owner=None
    ):
        self.window = window
        self.window_rect = self.window.get_rect()
        self.owner = owner
        self.image = myFont.render(str(self.owner.score), False, color)
        self.rect = self.image.get_rect()
        self.rect.centerx = pos_x
        self.rect.centery = pos_y
        self.color = color

    def update(self):
        self.image = myFont.render(str(self.owner.score), False, self.color)
        self.window.blit(self.image, self.rect)