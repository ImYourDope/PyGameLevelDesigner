from XMLparser import XMLParser
from dom import layout_manager
from state_manager import state_manager
from spritesheetloader import load_spritesheet

import tkinter
import tkinter.filedialog
import pygame

xml = XMLParser('layouts/spritesheetloader/spritesheetloader.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())


def init(props):
    """Initializes tkinter and spritesheet loader."""
    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    print(file_name)

    if not file_name:
        layout_manager.pop()
    else:
        tiles = load_spritesheet(file_name)

        print(tiles)
        layout.set('tiles', tiles)
        layout.get_element_by_id('current-loading-tile').elem.update_image(tiles[0])
        layout.set('counter', 0)
        layout.get_element_by_id('spritesheet-tile-counter').elem.set_text('1/{0}'.format(len(tiles)))


def next_elem(_, load_tile):
    """Switches to the next tile or skips it based on load_tile value."""

    if layout.get_element_by_id('input-tile_name').elem.text != '' or not load_tile:
        counter = layout.get('counter')
        tiles = layout.get('tiles')

        if load_tile:
            name = layout.get_element_by_id('input-tile_name').elem.text
            state_manager.get('DOM tile list').elem.append(tiles[counter], name)
            state_manager.get('DOM tile list').elem.update_surface()

        counter += 1

        if counter >= len(tiles):
            layout_manager.pop()
            return
        elif counter == len(tiles) - 1:
            layout.get_element_by_id('next-tile').elem.set_text('DONE')

        layout.get_element_by_id('current-loading-tile').elem.update_image(tiles[counter])
        layout.get_element_by_id('spritesheet-tile-counter').elem.set_text('{0}/{1}'.format(counter + 1, len(tiles)))
        layout.get_element_by_id('input-tile_name').elem.zero()
        layout.set('counter', counter)


layout.set('init', init)
layout.onclick('next-tile', lambda e: next_elem(e, load_tile=True))
layout.onclick('skip-tile', lambda e: next_elem(e, load_tile=False))
