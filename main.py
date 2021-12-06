from userinterface import *
from canvas import *
from EventManager import eventManager
from XMLparser import XMLParser
from DOM.Layout import layout_manager
from DOM.DOMEventElement import DOMEventElement
from Interface import Grid

from sys import exit
import pygame

pygame.init()

xml = XMLParser('interface.xml')
info = xml.read_metadata()

screen = pygame.display.set_mode((info['width'], info['height']))
pygame.display.set_caption('PyGame Level Designer')
clock = pygame.time.Clock()

root = xml.read_dom()
root.id = 'root'
grid = Grid({})

root.onclick('toggle-grid', grid.toggle_grid)

xml = XMLParser('tileloaderlayout.xml')
popup = xml.read_dom()
popup.onclick('close-popup', lambda _: layout_manager.pop())

root.onclick('open-test-screen-button', lambda _: layout_manager.push(popup))

create_scrolling_cursors()

layout_manager.push(root)

while True:

    # DRAW SECTION

    draw_ui_background(screen)
    draw_canvas(screen)
    if eventManager.grid_on:
        grid.draw(screen)
    draw_ui(screen)



    layout_manager.draw(screen)

    if eventManager.main_screen_on:
        draw_scrolling_cursor(screen)

    # EVENT SECTION
    for event in pygame.event.get():
        if eventManager.main_screen_on:
            scroll_canvas(event)

        if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION):
            layout_manager.process_event(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    clock.tick(FPS)
    pygame.display.update()
