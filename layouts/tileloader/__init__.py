from XMLparser import XMLParser
from DOM import layout_manager
from EventManager import event_manager

import tkinter
import tkinter.filedialog
import pygame

xml = XMLParser('layouts/tileloader/tileloader.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())


def init(props):
    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    print(file_name)
    if file_name == ():
        layout_manager.pop()
    else:
        tile = pygame.image.load(file_name)
        layout.set('tile', tile)
        layout.get_element_by_id('current-loading-tile').elem.update_image(tile)


def save_tile(_):
    event_manager.DOM_tile_list.elem.list.append(layout.get('tile'))
    event_manager.DOM_tile_list.elem.update_surface()
    layout_manager.pop()


layout.onclick('save-tile', save_tile)

# def delete(layout):
#     pass

layout.set('init', init)
