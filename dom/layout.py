import pygame
from random import randint
from dom import DOMEventElement, layout_manager
from settings import ui_main_color, popup_screen_border_color


class Layout:
    DEFAULT = {
        'x': 0,
        'y': 0,
        'width': 200,
        'height': 200
    }

    def __init__(self, dom, properties):
        self.id = properties['id'] if 'id' in properties else str(randint(0, 10 ** 10))
        self.properties = properties
        self.dom = dict()
        self.data = {
            'object in focus': None
        }
        self.state = {}

        self.set('init', lambda _: print('init'))
        self.set('delete', lambda: print('delete'))

        for elem in dom:
            self.dom[elem.id] = DOMEventElement(elem)

    def init(self, properties):
        self.get('init')(properties)

    def delete(self):
        self.get('delete')()

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

    def get_element_by_id(self, id):
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

    def pos_to_dict(self, cors):
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
                if elem.mouse_collision(layout_manager.absolute_pos_to_relative_pos(pygame.mouse.get_pos())):
                    elem.process_event('click', event)
                    self.change_focus(elem.id)
                    break
            else:
                self.change_focus(None)
        elif event.type == pygame.MOUSEMOTION:
            for elem in self.dom.values():
                if elem.mouse_collision(layout_manager.absolute_pos_to_relative_pos(pygame.mouse.get_pos())):
                    elem.props['hover'] = True
                    elem.process_event('hover', event)
                else:
                    elem.props['hover'] = False
        elif event.type == pygame.MOUSEWHEEL:
            for elem in self.dom.values():
                if elem.props['hover']:
                    elem.process_event('scroll', event)

    def disable(self):
        self.change_focus(None)
        for elem in self.dom.values():
            elem.props['hover'] = False

    def rect(self):
        return (self.properties['width'],
                self.properties['height'])

    def pos(self):
        return (self.properties['x'],
                self.properties['y'])

    def set(self, var, value):
        self.state[var] = value

    def get(self, var):
        return self.state[var]

    def reset(self):
        self.state = {}

    def draw(self, screen):
        if 'id' not in self.__dict__ or self.id != 'root':
            surface = pygame.Surface(self.rect())
            surface.fill(ui_main_color)
            rect = surface.get_rect()
            pygame.draw.rect(surface, popup_screen_border_color, rect, 5)
            # pygame.draw.rect(screen, ui_main_color, self.rect())
            for elem in self.dom.values():
                elem.draw(surface)
            screen.blit(surface, self.pos())
        else:
            for elem in self.dom.values():
                elem.draw(screen)
