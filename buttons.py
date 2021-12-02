from buttonclass import *
from grid import grid_button
from popupscreens import *


def create_popup_screen_buttons(screen):
    test_popup_screen_buttons.append(Button(screen, 'CLOSE TEST SCREEN', (200, 200), popup_screen_close, 15, 0))


def create_main_screen_buttons(screen):
    global test_popup_screen
    print(test_popup_screen)
    main_screen_buttons.append(
        Button(screen, 'OPEN TEST SCREEN', (10, starting_button_pos), test_popup_screen.open, 15, 0))
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
    state['active_buttons'] = main_screen_buttons



