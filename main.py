from sys import exit

import pygame

from userinterface import *
from canvas import *
from grid import *
# from inputlines import *
# from popupscreens import *

from event_manager import event_manager
from XML_parser import XMLParser
from Layout import Layout, layout_manager

event_manager.test_popup_screen = "hello"

pygame.init()

xml = XMLParser('interface.xml')
info = xml.read_metadata()

screen = pygame.display.set_mode((info['width'], info['height']))
pygame.display.set_caption('PyGame Level Designer')
clock = pygame.time.Clock()

root = xml.read_dom()

xml = XMLParser('popup.xml')
popup = xml.read_dom()
popup.onclick('close-popup', lambda _: layout_manager.pop())



root.onclick('open-test-screen-button', lambda _: layout_manager.push(popup))

# CREATE SECTION
# create_popup_screen_buttons(screen)
# create_popup_screen_inputlines(screen)
# create_popup_screens(screen)
# create_main_screen_buttons(screen)
# create_main_screen_inputlines(screen)
create_scrolling_cursors()

# dom_event_manager.oninput('input', lambda _: print(dom[2].text))
# create_main_screen_buttons("pohui")

layout_manager.push(root)

while True:

    # DRAW SECTION
    draw_ui_background(screen)
    draw_canvas(screen)
    if event_manager.grid_on:
        draw_grid(screen)
    draw_ui(screen)

    layout_manager.draw(screen)

    if event_manager.main_screen_on:
        draw_scrolling_cursor(screen)

    # EVENT SECTION
    for event in pygame.event.get():
        if event_manager.main_screen_on:
            scroll_canvas(event)

        if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION):
            layout_manager.process_event(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    clock.tick(FPS)
    pygame.display.update()
