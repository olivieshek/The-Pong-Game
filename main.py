import pygame
from paddle import Paddle
from ball import Ball
from score import Score

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(1)
pygame.mixer.music.load('assets/sound.mp3')
window = pygame.display.set_mode((800, 600))
window_rect = window.get_rect()
clock = pygame.time.Clock()
pygame.display.set_caption('The Pong Game')
# background = pygame.image.load('assets/background.png')
player = Paddle(window)
opponent = Paddle(window, isAuto=True)
ball = Ball(window)
player_score = Score(
    window,
    pos_x=window_rect.center[0] - 48,
    pos_y=window_rect.midtop[1] + 48,
    owner=player
)
opponent_score = Score(
    window,
    pos_x=window_rect.center[0] + 48,
    pos_y=window_rect.midtop[1] + 48,
    owner=opponent
)

running = True
while running:
    window.fill((0, 0, 0))
    # window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        keys = pygame.key.get_pressed()

    player.draw()
    player.controls(keys, ball)
    player_score.update()
    opponent.draw()
    opponent.controls(keys, ball)
    opponent_score.update()
    ball.draw()
    ball.movement(player, opponent)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()