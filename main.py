import pygame
from sys import exit
from settings import *
from spritesheetloader import *
from userinterface import *


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PyGame Level Designer')
clock = pygame.time.Clock()


while True:
    draw_ui(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(FPS)
    pygame.display.update()
