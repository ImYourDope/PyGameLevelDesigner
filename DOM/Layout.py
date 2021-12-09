import pygame

from EventManager import Singleton
from DOM.DOMEventElement import DOMEventElement
from settings import ui_main_color


class Layout:
    DEFAULT = {
        'x': 0,
        'y': 0,
        'width': 200,
        'height': 200
    }

    def __init__(self, dom, properties):
        self.properties = properties
        self.dom = dict()
        self.data = {
            'object in focus': None
        }
        for elem in dom:
            self.dom[elem.id] = DOMEventElement(elem)

    def on(self, action, id, callback):
        if id not in self.dom:
            raise Exception('Incorrect ID')
        self.dom[id].on(action, callback)

    def onclick(self, id, callback):
        self.on('click', id, callback)

    def onhover(self, id, callback):
        self.on('hover', id, callback)

    def oninput(self, id, callback):
        self.on('input', id, callback)

    def onchange(self, id, callback):
        self.on('change', id, callback)


    def getElementByID(self, id):
        if id in self.dom:
            return self.dom[id]

        raise Exception("Unknown id")

    def infocus(self, id):
        if id not in self.dom:
            return False
        return self.data['object in focus'] == id

    def ishovered(self, id):
        if id not in self.dom:
            return False
        return self.dom[id].props['hover']

    def elem_collision(self, id, cors):
        return self.dom[id].mouse_collision(cors)

    def change_focus(self, new_focus):
        old_focus = self.data['object in focus']
        self.data['object in focus'] = new_focus

        if old_focus is not None:
            prev = self.dom[old_focus]
            prev.process_event('unfocus')

        if new_focus is not None:
            next = self.dom[new_focus]
            next.process_event('focus')

    def cors_to_dict(self, cors):
        return {
            'x': cors[0],
            'y': cors[1]
        }

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.data['object in focus'] is not None:
                self.dom[self.data['object in focus']].process_event('input', event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for elem in self.dom.values():
                if elem.mouse_collision(layout_manager.cors_to_relative_pos(pygame.mouse.get_pos())):
                    elem.process_event('click', event)
                    self.change_focus(elem.id)
                    break
            else:
                self.change_focus(None)
        elif event.type == pygame.MOUSEMOTION:
            for elem in self.dom.values():
                if elem.mouse_collision(layout_manager.cors_to_relative_pos(pygame.mouse.get_pos())):
                    elem.props['hover'] = True
                    elem.process_event('hover', event)
                else:
                    elem.props['hover'] = False

    def disable(self):
        self.change_focus(None)
        for elem in self.dom.values():
            elem.props['hover'] = False

    def rect(self):
        return (self.properties['width'],
                self.properties['height'])

    def cors(self):
        return (self.properties['x'],
                self.properties['y'])

    def draw(self, screen):
        if 'id' not in self.__dict__ or self.id != 'root':
            surface = pygame.Surface(self.rect())
            surface.fill(ui_main_color)
            # pygame.draw.rect(screen, ui_main_color, self.rect())
            for elem in self.dom.values():
                elem.draw(surface)
            screen.blit(surface, self.cors())
        else:
            for elem in self.dom.values():
                elem.draw(screen)


class LayoutManager(Singleton):
    layouts = []

    def push(self, layout):
        if self.last() is not None:
            self.last().disable()
        self.layouts.append(layout)

    def pop(self):
        self.layouts.pop()

    def last(self):
        if len(self.layouts) > 0:
            return self.layouts[len(self.layouts) - 1]
        return None

    def cors_to_relative_pos(self, cors):
        new_cors = [*cors]
        for layout in self.layouts:
            new_cors[0] -= layout.properties['x']
            new_cors[1] -= layout.properties['y']
        return new_cors

    def process_event(self, event):
        self.last().process_event(event)

    def infocus(self, id):
        return self.last().infocus(id)

    def ishovered(self, id):
        return self.last().ishovered(id)

    def draw(self, screen):
        for layout in self.layouts:
            layout.draw(screen)


layout_manager = LayoutManager()
