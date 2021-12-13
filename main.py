from userinterface import *
from canvas import *
from EventManager import eventManager
from Interface import Grid
from XMLparser import XMLParser
from DOM import layout_manager

# WARNING: layouts module imports dynamically. Don't change this part of code if you don't understand what it does
from layout_loader import init_layouts
init_layouts()
from layouts import *
# END OF WARNING


from spritesheetloader import load_spritesheet


from sys import exit
import pygame

pygame.init()

xml = XMLParser('main.xml')
info = xml.read_metadata()

screen = pygame.display.set_mode((info['width'], info['height']))
pygame.display.set_caption('PyGame Level Designer')
clock = pygame.time.Clock()

root = xml.read_dom()
root.id = 'root'
grid = Grid({})


spritesheets_blocks = load_spritesheet('TX_Tileset_Grass.png')
spritesheets = []
for spritesheet_block in spritesheets_blocks:
    spritesheets.extend(spritesheet_block)

eventManager.spritesheets = spritesheets
spritesheetloader.get_element_by_id('current-loading-tile').elem.update_image(spritesheets[0])



root.onclick('toggle-grid', grid.toggle_grid)
root.onclick('open-test-screen-button', lambda _: layout_manager.push(spritesheetloader))





# popup.getElementByID('current-loading-tile').elem.update_image(tmp)

# root.onclick('open-test-screen-button', lambda _: layout_manager.push())

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

    # if eventManager.main_screen_on:
    #     draw_scrolling_cursor(screen)

    # EVENT SECTION
    for event in pygame.event.get():
        # if eventManager.main_screen_on:
        #     scroll_canvas(event)
        print(event)
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
