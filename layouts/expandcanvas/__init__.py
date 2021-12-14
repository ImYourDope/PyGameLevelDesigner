from XMLparser import XMLParser
from dom import layout_manager
from canvas import *
from interface import Grid

xml = XMLParser('layouts/expandcanvas/expandcanvas.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())


def expand_wrapper(_):
    button_ids = ('left-expand-input', 'right-expand-input', 'top-expand-input', 'bottom-expand-input')
    sides = [None] * 4
    for i in range(len(button_ids)):
        if layout.get_element_by_id(button_ids[i]).elem.text == '':
            sides[i] = 0
        else:
            sides[i] = int(layout.get_element_by_id(button_ids[i]).elem.text)
    event_manager.canvas.expand(*sides)
    event_manager.grid = Grid(event_manager.canvas)
    layout_manager.pop()


layout.onclick('ok-expand', expand_wrapper)
