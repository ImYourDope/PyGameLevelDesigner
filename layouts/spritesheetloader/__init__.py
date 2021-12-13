from XMLparser import XMLParser
from DOM import layout_manager
from EventManager import event_manager

xml = XMLParser('layouts/spritesheetloader/spritesheetloader.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())

event_manager.current_spritesheet_number = 0
event_manager.done = False

def next_tile(_):
    n = event_manager.current_spritesheet_number

    if event_manager.done:
        return

    if n + 1 >= len(event_manager.spritesheets):
        layout.get_element_by_id('next-tile').elem.set_text('DONE')
        layout.get_element_by_id('next-tile').onclick(lambda _: layout_manager.pop())
        event_manager.done = True
    else:
        layout.get_element_by_id('current-loading-tile').elem.update_image(event_manager.spritesheets[n + 1])
        event_manager.current_spritesheet_number = n + 1


layout.onclick('next-tile', next_tile)
