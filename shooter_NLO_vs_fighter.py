import pygame

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Awesome Shooter Game")

fighter_image = pygame.image.load('images/fighter.png')

fighter_width, fighter_heigh = fighter_image.get_size()