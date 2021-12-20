from settings import *
from state_manager import *
from dom import layout


def text_buttons_update(layout, boollist):
    i = 0
    for button_id in main_screen_buttons_id:
        state_manager.set(button_id+'state', boollist[i])
        layout.get_element_by_id(button_id).elem.update()
        i += 1