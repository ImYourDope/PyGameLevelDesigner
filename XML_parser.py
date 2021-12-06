import xml.etree.ElementTree as ET
from random import randint

from Interface import *
from Layout import Layout


class XMLParser:
    def __init__(self, filepath):

        xml = ET.parse(filepath)
        self.root = xml.getroot()
        if self.root.tag != 'Layout':
            raise Exception("Incorrect XML. Should start from <Layout> tag")

    def read_metadata(self):
        return XMLParser.convert_props(self.root.attrib)

    def read_dom(self):
        dom = []
        for elem in self.root:
            props = XMLParser.read_properties(elem)
            XMLParser.convert_props(props)
            XMLParser.set_id(props)

            if elem.tag == 'Button':
                props = XMLParser.set_default_parameters(props, Button.DEFAULT)
                dom.append(Button(props))
            elif elem.tag == 'Input':
                props = XMLParser.set_default_parameters(props, Input.DEFAULT)
                dom.append(Input(props))
            else:
                raise Exception('Incorrect tag')
        return Layout(dom)

    @staticmethod
    def convert_props(props):
        for key in 'x', 'y', 'width', 'height':
            if key in props:
                props[key] = int(props[key])
        for key in props.keys():
            if type(props[key]) is dict:
                XMLParser.convert_props(props[key])

        return props

    @staticmethod
    def read_properties(elem):
        hover = elem.find('Hover')
        if hover is not None:
            elem.attrib['hover'] = hover.attrib

        return elem.attrib

    @staticmethod
    def set_id(props):
        if 'id' not in props:
            props['id'] = str(randint(0, 10000000000))

    @staticmethod
    def set_default_parameters(props, default):
        for key in default.keys():
            if not key in props:
                props[key] = default[key]
            else:
                if type(props[key]) is dict:
                    XMLParser.set_default_parameters(props[key], default[key])
        return props


ml = XMLParser('interface.xml')
