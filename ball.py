import pygame

class Ball:
    def __init__(
        self,
        window,
        velocity_x=6,
        velocity_y=-6
    ):
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.window = window
        self.window_rect = self.window.get_rect()
        self.rect.centerx = self.window.get_width() / 2
        self.rect.centery = self.window.get_height() / 2
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def draw(self):
        self.window.blit(self.image, self.rect)

    def movement(self, player, opponent):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        if self.rect.right >= self.window_rect.right:
            self.velocity_x *= -1
        if self.rect.left <= self.window_rect.left:
            self.velocity_x *= -1
        if self.rect.top <= self.window_rect.top:
            self.velocity_y *= -1
        if self.rect.bottom >= self.window_rect.bottom:
            self.velocity_y *= -1

        if self.rect.colliderect(player.rect):
            self.velocity_x *= -1
            self.velocity_y *= -1
        if self.rect.colliderect(opponent.rect):
            self.velocity_x *= -1
            self.velocity_y *= -1