from buttonclass import *
from grid import grid_button
# from popupscreens import open_test_popup_screen, close_popup_screen

main_screen_buttons = []
popup_screen_buttons = []
active_buttons = main_screen_buttons
test_popup_screen_buttons = []


def create_buttons(screen):
    #main_screen_buttons.append(
        # Button(screen, 'CREATE PROJECT', (10, starting_button_pos), open_test_popup_screen, 15, 0))
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
    # test_popup_screen_buttons.append(
        #Button(screen, 'CLOSE POP UP SCREEN', (0, 0), close_popup_screen, 15, 0)
   # )


def update_buttons():
    global active_buttons
    if state['main_screen']:
        active_buttons = main_screen_buttons
    elif state['popup_screen']:
        active_buttons = popup_screen_buttons
