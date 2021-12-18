from sys import exit

from dom import layout_manager
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

state_manager.set('screen', screen)

root = xml.read_dom()
root.id = 'root'

state_manager.set('spritesheets', [])

root.onclick('toggle-grid', Grid.toggle_grid)
root.onclick('create-project-button', lambda _: layout_manager.push(projectcreate))
root.onclick('expand-canvas-button', lambda _: layout_manager.push(expandcanvas))

root.onclick('load-tiles-button', lambda _: layout_manager.push(tileloader))
root.onclick('load-spritesheet-button', lambda _: layout_manager.push(spritesheetloader))

state_manager.set('DOM tile list', root.get_element_by_id('tiles'))

create_scrolling_cursors()

layout_manager.push(root)

while True:
    # DRAW SECTION
    draw_ui_background(screen)
    if state_manager.get('project created'):
        state_manager.get('canvas').draw()
    draw_ui(screen)

    layout_manager.draw(screen)

    if layout_manager.last().id == "root" and state_manager.get('project created'):
        state_manager.get('canvas').draw_scrolling_cursor()

    # EVENT SECTION
    for event in pygame.event.get():
        if layout_manager.last().id == "root" \
                and state_manager.get('project created'):
            state_manager.get('canvas').scroll(event)

        if event.type in (pygame.KEYDOWN, pygame.MOUSEMOTION, pygame.MOUSEWHEEL):
            layout_manager.process_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                layout_manager.process_event(event)
                if state_manager.get('canvas') is not None:
                    state_manager.get('canvas').onclick(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    clock.tick(FPS)
    pygame.display.update()
