import pygame
from PIL import Image
from paddle import Paddle
from ball import Ball

pygame.init()
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('The Pong Game')
background = pygame.image.load('assets/background.png')
player = Paddle(window)
opponent = Paddle(window, isAuto=True)
ball = Ball(window)

running = True
while running:
    window.fill((0, 0, 0))
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        keys = pygame.key.get_pressed()

    player.draw()
    player.controls(keys)
    opponent.draw()
    opponent.controls(keys)
    ball.draw()
    ball.movement()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()