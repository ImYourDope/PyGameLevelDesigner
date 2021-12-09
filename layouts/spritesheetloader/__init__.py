from XMLparser import XMLParser
from DOM import layout_manager
from EventManager import eventManager

xml = XMLParser('layouts/spritesheetloader/spritesheetloader.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())

eventManager.current_spritesheet_number = 0


def next_tile(_):
    n = eventManager.current_spritesheet_number
    if n + 1 >= len(eventManager.spritesheets):
        layout.getElementByID('next-tile').elem.setText('DONE')
        return
    layout.getElementByID('current-loading-tile').elem.update_image(eventManager.spritesheets[n + 1])
    eventManager.current_spritesheet_number = n + 1


layout.onclick('next-tile', next_tile)
