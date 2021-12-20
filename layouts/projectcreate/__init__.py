from dom import layout_manager
from canvas import *
from supportfunctions import *

xml = XMLParser('layouts/projectcreate/projectcreate.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())


def create_project(_):
    """Creates project and initializes some states."""

    if layout.get_element_by_id('input-project-name').elem.text != '' and \
            int(layout.get_element_by_id('input-canvas-width').elem.text) > 0 and \
            int(layout.get_element_by_id('input-canvas-height').elem.text) > 0:

        state_manager.set('active_canvas', Canvas(state_manager.get('screen'),
                                                  int(layout.get_element_by_id('input-canvas-width').elem.text),
                                                  int(layout.get_element_by_id('input-canvas-height').elem.text)))

        state_manager.set('inactive_canvas', Canvas(state_manager.get('screen'),
                                                    int(layout.get_element_by_id('input-canvas-width').elem.text),
                                                    int(layout.get_element_by_id('input-canvas-height').elem.text)))

        state_manager.set('project name', layout.get_element_by_id('input-project-name').elem.text)
        state_manager.set('project created', True)
        state_manager.set('main_on', True)
        layout.get_element_by_id('input-project-name').elem.zero()
        layout.get_element_by_id('input-canvas-width').elem.zero()
        layout.get_element_by_id('input-canvas-height').elem.zero()
        layout_manager.pop()
        xml = XMLParser('main.xml')
        text_buttons_update(xml.read_dom(), main_buttons_state)


layout.onclick('ok-create-project', create_project)
