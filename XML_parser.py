import xml.etree.ElementTree as ET
from random import randint

from Interface import *


class XMLParser:
    def __init__(self, filepath):

        xml = ET.parse(filepath)
        self.root = xml.getroot()
        if self.root.tag != 'Layout':
            raise Exception("Incorrect XML. Should start from <Layout> tag")

    def read_metadata(self):
        return XMLParser.convert_props(self.root.attrib)

    def read_dom(self, surface):
        dom = []
        for elem in self.root:
            if elem.tag == 'Button':
                hover = elem.find('Hover')
                if hover is not None:
                    elem.attrib['hover'] = XMLParser.convert_props(hover.attrib)
                if 'id' not in elem.attrib:
                    elem.attrib['id'] = str(randint(0, 10000000000))
                dom.append(Button(surface, XMLParser.convert_props(elem.attrib)))
            elif elem.tag == 'Input':
                dom.append(Input(surface, XMLParser.convert_props(elem.attrib)))
            else:
                raise Exception('Incorrect tag')
            print(elem.tag)
            print(elem.attrib)
        return dom

    @staticmethod
    def convert_props(props):
        for key in 'x', 'y', 'width', 'height':
            if key in props:
                props[key] = int(props[key])
        return props


ml = XMLParser('interface.xml')
