from XMLparser import XMLParser
from DOM import layout_manager
from EventManager import event_manager
from canvas import Canvas
from Interface import Grid


xml = XMLParser('layouts/projectcreate/projectcreate.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())


def create_project(_):
    if layout.get_element_by_id('input-project-name').elem.text != '' and \
            int(layout.get_element_by_id('input-canvas-width').elem.text) > 0 and \
            int(layout.get_element_by_id('input-canvas-height').elem.text) > 0:
        event_manager.canvas = Canvas(event_manager.screen,
                                      int(layout.get_element_by_id('input-canvas-width').elem.text),
                                      int(layout.get_element_by_id('input-canvas-height').elem.text))
        event_manager.grid = Grid(event_manager.canvas)
        event_manager.project_name = layout.get_element_by_id('input-project-name').elem.text
        event_manager.project_created = True
        layout_manager.pop()


layout.onclick('ok-create-project', create_project)
