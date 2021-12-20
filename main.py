from sys import exit
from canvas import *
from dom import layout_manager
from load_and_save import save, load
from userinterface import *
from supportfunctions import *
# WARNING: layouts module imports dynamically. Don't change this part of code if you don't understand what it does
from layout_loader import init_layouts
init_layouts()
from layouts import *
# END OF WARNING

pygame.init()

# CREATING MAIN OBJECTS
xml = XMLParser('main.xml')
info = xml.read_metadata()
screen = pygame.display.set_mode((info['width'], info['height']))
pygame.display.set_caption('PyGame Level Designer')
clock = pygame.time.Clock()
state_manager.set('screen', screen)
root = xml.read_dom()
root.id = 'root'
state_manager.set('spritesheets', [])


def add_onclick(id, fn):
    """Function for simplified syntax. Checks the button state."""

    def new_fn(e):
        if state_manager.get(id + 'state'):
            fn(e)

    root.onclick(id, new_fn)


# ASSIGNING FUNCTIONS TO BUTTONS
add_onclick('toggle-grid', Grid.toggle_grid)
add_onclick('create-project-button', lambda _: layout_manager.push(projectcreate))
add_onclick('load-tiles-button', lambda _: layout_manager.push(tileloader))
add_onclick('load-spritesheet-button', lambda _: layout_manager.push(spritesheetloader))
add_onclick('collision-button', lambda _: switch_canvas())
add_onclick('expand-canvas-button', lambda _: layout_manager.push(expandcanvas))

root.oninput('tile-library-search-line', lambda _: state_manager.get('DOM tile list').elem.set_search(
    root.get_element_by_id('tile-library-search-line').elem.text
))

root.onclick('save-project-button', save)
root.onclick('load-project-button', load)


state_manager.set('DOM tile list', root.get_element_by_id('tiles'))
state_manager.set('root', root)

# STARTING FUNCTIONS
create_scrolling_cursors()
layout_manager.push(root)
text_buttons_update(xml.read_dom(), start_buttons_state)

while True:
    # DRAW SECTION
    draw_ui_background(screen)

    if state_manager.get('project created'):
        state_manager.get('active_canvas').draw()
    draw_ui(screen)

    layout_manager.draw(screen)

    if layout_manager.last().id == "root" and state_manager.get('project created'):
        state_manager.get('active_canvas').draw_scrolling_cursor()

    # EVENT SECTION
    for event in pygame.event.get():

        if layout_manager.last().id == "root" \
                and state_manager.get('project created'):
            state_manager.get('active_canvas').scroll(event)

        if event.type in (pygame.KEYDOWN, pygame.MOUSEMOTION, pygame.MOUSEWHEEL):
            layout_manager.process_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            layout_manager.process_event(event)
            if state_manager.get('active_canvas') is not None:
                state_manager.get('active_canvas').onclick(event)

        # QUIT SECTION
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # TICK SECTION
    clock.tick(FPS)
    pygame.display.update()
