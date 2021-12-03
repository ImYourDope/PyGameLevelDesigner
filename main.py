from sys import exit

import pygame

from userinterface import *
from canvas import *
from grid import *
from buttons import *
# from inputlines import *
# from popupscreens import *

from event_manager import event_manager, dom_event_manager
from XML_parser import XMLParser

event_manager.test_popup_screen = "hello"

pygame.init()

xml = XMLParser('interface.xml')
info = xml.read_metadata()

screen = pygame.display.set_mode((info['width'], info['height']))
pygame.display.set_caption('PyGame Level Designer')
clock = pygame.time.Clock()

dom = xml.read_dom(screen)

dom_event_manager.init_dom(dom)

# dom_event_manager.onclick('grid-button', toggle_grid)

# CREATE SECTION
# create_popup_screen_buttons(screen)
# create_popup_screen_inputlines(screen)
# create_popup_screens(screen)
# create_main_screen_buttons(screen)
# create_main_screen_inputlines(screen)
create_scrolling_cursors()

# dom_event_manager.oninput('input', lambda _: print(dom[2].text))
# create_main_screen_buttons("pohui")

while True:

    # DRAW SECTION
    draw_ui_background(screen)
    draw_canvas(screen)
    if event_manager.grid_on:
        draw_grid(screen)
    draw_ui(screen)

    for elem in dom:
        elem.draw()

    # if event_manager.popup_screen_on:
    #     event_manager.popup_screen.draw()
    # if event_manager.main_screen_on:
    #     draw_scrolling_cursor(screen)

    # EVENT SECTION
    for event in pygame.event.get():
        if event_manager.main_screen_on:
            scroll_canvas(event)

        if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION):
            dom_event_manager.process_event(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    clock.tick(FPS)
    pygame.display.update()
