from popupscreenclass import *


def create_popup_screens(screen):
    global test_popup_screen
    test_popup_screen = PopupScreen(screen, (100, 0, 500, 500), test_popup_screen_buttons, test_popup_screen_inputlines)