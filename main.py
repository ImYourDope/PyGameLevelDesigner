from sys import exit
from userinterface import *
from canvas import *
from grid import *
from buttons import *
from inputlines import *
from popupscreens import *


pygame.init()

# CREATE SECTION
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PyGame Level Designer')
clock = pygame.time.Clock()
create_buttons(screen)
create_inputlines(screen)
# create_popup_screens(screen)
create_scrolling_cursors()

while True:

    # DRAW SECTION
    draw_ui_background(screen)
    draw_canvas(screen)
    if state['grid_on']:
        draw_grid(screen)
    draw_ui(screen)
    for b in main_screen_buttons:
        b.draw()
    for i in main_screen_inputlines:
        i.draw()
    if state['popup_screen']:
        popup_screen.draw()
    if state['main_screen']:
        draw_scrolling_cursor(screen)

    # EVENT SECTION
    for event in pygame.event.get():
        if state['main_screen']:
            scroll_canvas(event)
        for b in active_buttons:
            b.click(event)
        for i in active_inputlines:
            i.process(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # UPDATE SECTION
    for i in active_inputlines:
        i.update_text_surface()
    update_buttons()
    update_inputlines()
    clock.tick(FPS)
    pygame.display.update()
