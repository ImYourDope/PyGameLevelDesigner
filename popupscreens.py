from popupscreenclass import *

from event_manager import event_manager

def create_popup_screens(screen):
    event_manager.test_popup_screen = PopupScreen(screen, (100, 0, 500, 500), test_popup_screen_buttons, test_popup_screen_inputlines)