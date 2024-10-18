import pygame
from src.config import config

pygame.init()
screen = pygame.display.set_mode(
    (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("magenta")
    pygame.display.flip()
    clock.tick(config.FPS)
