from dom import layout_manager
from canvas import *

xml = XMLParser('layouts/expandcanvas/expandcanvas.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())


def expand_wrapper(_):
    """Reads the input data and expands the canvases."""
    button_ids = ('left-expand-input', 'right-expand-input', 'top-expand-input', 'bottom-expand-input')
    sides = [None] * 4

    for i in range(len(button_ids)):
        if layout.get_element_by_id(button_ids[i]).elem.text == '':
            sides[i] = 0
        else:
            sides[i] = int(layout.get_element_by_id(button_ids[i]).elem.text)

    state_manager.get('active_canvas').expand(*sides)
    state_manager.get('inactive_canvas').expand(*sides)

    for button_id in button_ids:
        layout.get_element_by_id(button_id).elem.zero()
    layout_manager.pop()


layout.onclick('ok-expand', expand_wrapper)
