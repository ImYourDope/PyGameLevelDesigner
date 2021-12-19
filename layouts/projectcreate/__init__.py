from XMLparser import XMLParser
from dom import layout_manager
from canvas import *
from layouts import expandcanvas

xml = XMLParser('layouts/projectcreate/projectcreate.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())


def create_project(_):
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
        state_manager.get('root').onclick('collision-button', switch_canvas())
        state_manager.get('root').onclick('expand-canvas-button', lambda _: layout_manager.push(expandcanvas))
        layout.get_element_by_id('input-project-name').elem.zero()
        layout.get_element_by_id('input-canvas-width').elem.zero()
        layout.get_element_by_id('input-canvas-height').elem.zero()
        layout_manager.pop()


layout.onclick('ok-create-project', create_project)
