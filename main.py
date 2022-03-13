import pygame
from PIL import Image
import paddle as pd
import ball as bl

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('The Pong Game')
playerImage = Image.open('assets/player.png')
player_PGimage = pygame.image.load('assets/player.png')
player = pd.Paddle(
    window,
    window.get_width() / 50 + playerImage.width / 2,
    player_PGimage
)
opponentImage = Image.open('assets/opponent.png')
opponent_PGimage = pygame.image.load('assets/opponent.png')
opponent = pd.Paddle(
    window,
    window.get_width() - window.get_width() / 50 - opponentImage.width / 2,
    opponent_PGimage
)
ball = bl.Ball(window)

running = True
while running:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.rect.y -= player.speed
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.rect.y += player.speed

    player.draw()
    opponent.draw()
    ball.draw()
    pygame.display.flip()