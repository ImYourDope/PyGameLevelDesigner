from userinterface import *
from canvas import *
from EventManager import event_manager
from Interface import Grid
from XMLparser import XMLParser
from DOM import layout_manager
from spritesheetloader import load_spritesheet
from sys import exit
import pygame

# WARNING: layouts module imports dynamically. Don't change this part of code if you don't understand what it does
from layout_loader import init_layouts

init_layouts()
from layouts import *

# END OF WARNING


pygame.init()

xml = XMLParser('main.xml')
info = xml.read_metadata()

screen = pygame.display.set_mode((info['width'], info['height']))
pygame.display.set_caption('PyGame Level Designer')
clock = pygame.time.Clock()

root = xml.read_dom()
root.id = 'root'
grid = Grid({})

# spritesheets_blocks = load_spritesheet('testspritesheet.png')
# spritesheets = []
# for spritesheet_block in spritesheets_blocks:
#     spritesheets.extend(spritesheet_block)

event_manager.spritesheets = []

root.onclick('toggle-grid', grid.toggle_grid)
root.onclick('create-project-button', lambda _: layout_manager.push(projectcreate))
root.onclick('expand-canvas-button', lambda _: layout_manager.push(expandcanvas))

root.onclick('load-tiles-button', lambda _: layout_manager.push(tileloader))
root.onclick('load-spritesheet-button', lambda _: layout_manager.push(spritesheetloader))

root.get_element_by_id('tiles').elem.list = event_manager.spritesheets
root.get_element_by_id('tiles').elem.update_surface()

event_manager.DOM_tile_list = root.get_element_by_id('tiles')
# popup.getElementByID('current-loading-tile').elem.update_image(tmp)

# root.onclick('open-test-screen-button', lambda _: layout_manager.push())

create_scrolling_cursors()

layout_manager.push(root)

while True:
    # DRAW SECTION
    draw_ui_background(screen)
    draw_canvas(screen)
    if event_manager.grid_on:
        grid.draw(screen)
    draw_ui(screen)

    layout_manager.draw(screen)

    if event_manager.main_screen_on and layout_manager.last().id == "root":
        draw_scrolling_cursor(screen)

    # EVENT SECTION
    for event in pygame.event.get():
        if event_manager.main_screen_on and layout_manager.last().id == "root":
            scroll_canvas(event)
        if event.type in (pygame.KEYDOWN, pygame.MOUSEMOTION, pygame.MOUSEWHEEL):
            layout_manager.process_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                layout_manager.process_event(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    clock.tick(FPS)
    pygame.display.update()
