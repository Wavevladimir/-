import sys

import pygame
import sys


pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My Pygame")

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), (0, 0, 100, 200))
    pygame.display.update()

