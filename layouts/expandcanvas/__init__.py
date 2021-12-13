from XMLparser import XMLParser
from DOM import layout_manager

xml = XMLParser('layouts/expandcanvas/expandcanvas.xml')  # popup xml file
layout = xml.read_dom()
layout.onclick('close-popup', lambda _: layout_manager.pop())
