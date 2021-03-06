from XMLparser import XMLParser
from dom import layout_manager
from state_manager import state_manager

import tkinter
import tkinter.filedialog
import pygame

xml = XMLParser('layouts/tileloader/tileloader.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())


def init(props):
    """Initializes tkinter and tile loader."""

    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    print(file_name)

    if not file_name:
        layout_manager.pop()
    else:
        tile = pygame.image.load(file_name)
        layout.set('tile', tile)
        layout.get_element_by_id('current-loading-tile').elem.update_image(tile)


def save_tile(_):
    """Saves the tile and adds it to the tile list."""

    name = layout.get_element_by_id('input-tile_name').elem.text

    if name != '':
        state_manager.get('DOM tile list').elem.append(layout.get('tile'), name)
        state_manager.get('DOM tile list').elem.update_surface()
        layout.get_element_by_id('input-tile_name').elem.zero()
        layout_manager.pop()


layout.onclick('save-tile', save_tile)
layout.set('init', init)
