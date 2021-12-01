'''
from popupscreenclass import *
from inputlines import test_popup_screen_inputlines
from buttons import test_popup_screen_buttons


def close_popup_screen():
    state['popup_screen'] = False
    state['main_screen'] = True


def create_popup_screens(screen):
    global test_popup_screen
    test_popup_screen = PopUpScreen(screen, (0, 0, 500, 500), test_popup_screen_buttons, test_popup_screen_inputlines)


def open_test_popup_screen():
    test_popup_screen.create()
    '''
