from sys import exit

from dom import layout_manager
from interface import Grid
from XMLparser import XMLParser
from canvas import *
# WARNING: layouts module imports dynamically. Don't change this part of code if you don't understand what it does
from layout_loader import init_layouts
from userinterface import *

init_layouts()
from layouts import *

# END OF WARNING


pygame.init()

xml = XMLParser('main.xml')
info = xml.read_metadata()

screen = pygame.display.set_mode((info['width'], info['height']))
pygame.display.set_caption('PyGame Level Designer')
clock = pygame.time.Clock()

event_manager.screen = screen

root = xml.read_dom()
root.id = 'root'

event_manager.spritesheets = []

root.onclick('toggle-grid', Grid.toggle_grid)
root.onclick('create-project-button', lambda _: layout_manager.push(projectcreate))
root.onclick('expand-canvas-button', lambda _: layout_manager.push(expandcanvas))

root.onclick('load-tiles-button', lambda _: layout_manager.push(tileloader))
root.onclick('load-spritesheet-button', lambda _: layout_manager.push(spritesheetloader))

event_manager.DOM_tile_list = root.get_element_by_id('tiles')

create_scrolling_cursors()

layout_manager.push(root)

while True:
    # DRAW SECTION
    draw_ui_background(screen)
    if event_manager.project_created:
        event_manager.canvas.draw()
        if event_manager.grid_on:
            event_manager.grid.draw()

    draw_ui(screen)

    layout_manager.draw(screen)

    if event_manager.main_screen_on and layout_manager.last().id == "root" and event_manager.project_created:
        event_manager.canvas.draw_scrolling_cursor()

    # EVENT SECTION
    for event in pygame.event.get():
        if layout_manager.last().id == "root" \
                and event_manager.project_created:
            event_manager.canvas.scroll(event)

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
