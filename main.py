import pygame
from sys import exit
from settings import *
from spritesheetloader import *
from userinterface import *
from grid import *
from canvas import *
from buttons import *
from buttonclass import *


pygame.init()

# CREATE SECTION
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PyGame Level Designer')
clock = pygame.time.Clock()
create_buttons(screen)

while True:

    # print(grid_on)

    # DRAW SECTION
    draw_ui_background(screen)
    draw_canvas(screen)
    if grid_on:
        draw_grid(screen)
    draw_ui(screen)
    for b in buttons:
        b.draw()

    # EVENT SECTION
    for event in pygame.event.get():
        for b in buttons:
            b.click(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # UPDATE SECTION
    clock.tick(FPS)
    pygame.display.update()
