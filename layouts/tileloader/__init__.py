from XMLparser import XMLParser
from DOM import layout_manager

import tkinter
import tkinter.filedialog
import pygame

xml = XMLParser('layouts/tileloader/tileloader.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())


def init(props):
    print('hello there')
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    tile = pygame.image.load(file_name)
    layout.get_element_by_id('current-loading-tile').elem.update_image(tile)


# def delete(layout):
#     pass

layout.functions['init'] = init
