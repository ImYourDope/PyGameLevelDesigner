from sys import exit
from userinterface import *
from canvas import *
from grid import *
from buttons import *
from inputlines import *
from popupscreens import *

from event_manager import event_manager

event_manager.test_popup_screen = "hello"

pygame.init()

# CREATE SECTION
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PyGame Level Designer')
clock = pygame.time.Clock()
create_popup_screen_buttons(screen)
create_popup_screen_inputlines(screen)
create_popup_screens(screen)
create_main_screen_buttons(screen)
create_main_screen_inputlines(screen)
create_scrolling_cursors()

while True:

    # DRAW SECTION
    draw_ui_background(screen)
    draw_canvas(screen)
    if event_manager.grid_on:
        draw_grid(screen)
    draw_ui(screen)
    for b in main_screen_buttons:
        b.draw()
    for i in main_screen_inputlines:
        i.draw()
    if event_manager.popup_screen_on:
        event_manager.popup_screen.draw()
    if event_manager.main_screen_on:
        draw_scrolling_cursor(screen)

    # EVENT SECTION
    for event in pygame.event.get():
        if event_manager.main_screen_on:
            scroll_canvas(event)
        for b in event_manager.active_buttons:
            b.click(event)
        for i in event_manager.active_inputlines:
            i.process(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # UPDATE SECTION
    for i in event_manager.active_inputlines:
        i.update_text_surface()
    clock.tick(FPS)
    pygame.display.update()
