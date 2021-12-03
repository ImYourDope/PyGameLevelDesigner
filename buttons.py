from Interface.button import *
from grid import toggle_grid
from popupscreens import *

from event_manager import event_manager


def create_popup_screen_buttons(screen):
    test_popup_screen_buttons.append(Button(screen, 'CLOSE TEST SCREEN', (200, 200), popup_screen_close, 15, 0))


def create_main_screen_buttons(screen):

    print(event_manager.test_popup_screen)
    main_screen_buttons.append(
        Button(screen, 'OPEN TEST SCREEN', (10, starting_button_pos), event_manager.test_popup_screen.start, 15, 0))
    main_screen_buttons.append(
        Button(screen, 'LOAD PROJECT', (10, (button_gap + main_font_size) + starting_button_pos), grid_button, 15, 0))
    main_screen_buttons.append(
        Button(screen, 'SAVE PROJECT', (10, (button_gap + main_font_size) * 2 + starting_button_pos), grid_button, 15,
               0))
    main_screen_buttons.append(
        Button(screen, 'CREATE LAYER', (10, (button_gap + main_font_size) * 3 + starting_button_pos), grid_button, 15,
               0))
    main_screen_buttons.append(
        Button(screen, 'CREATE LEVEL', (10, (button_gap + main_font_size) * 4 + starting_button_pos), grid_button, 15,
               0))

    event_manager.active_buttons = main_screen_buttons



