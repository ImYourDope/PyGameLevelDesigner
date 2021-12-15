from XMLparser import XMLParser
from dom import layout_manager
from state_manager import state_manager
from canvas import Canvas
from interface import Grid


xml = XMLParser('layouts/projectcreate/projectcreate.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())


def create_project(_):
    if layout.get_element_by_id('input-project-name').elem.text != '' and \
            int(layout.get_element_by_id('input-canvas-width').elem.text) > 0 and \
            int(layout.get_element_by_id('input-canvas-height').elem.text) > 0:
        state_manager.canvas = Canvas(state_manager.screen,
                                      int(layout.get_element_by_id('input-canvas-width').elem.text),
                                      int(layout.get_element_by_id('input-canvas-height').elem.text))
        state_manager.grid = Grid(state_manager.canvas)
        state_manager.project_name = layout.get_element_by_id('input-project-name').elem.text
        state_manager.project_created = True
        layout_manager.pop()


layout.onclick('ok-create-project', create_project)
