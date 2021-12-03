import pygame.mouse

from settings import *
from .dom_element import DOMElement
from event_manager import dom_event_manager


class Button(DOMElement):
    DEFAULT = {
        'x': 0,
        'y': 0,
        'width': 200,
        'height': 28,
        'hover': {
            'position': 'relative',
            'x': 0,
            'y': 0
        }
    }

    def __init__(self, screen, properties):
        self.screen = screen
        self.id = properties['id']

        if properties['hover']['position'] == 'relative':
            properties['hover']['x'] += properties['x']
            properties['hover']['y'] += properties['y']

        self.surface = main_font.render(properties['text'], False, main_font_color)
        self.pos = (properties['x'], properties['y'])
        self.rect = self.surface.get_rect(topleft=self.pos)
        self.shift_pos = (properties['hover']['x'], properties['hover']['y'])
        self.shift_rect = self.surface.get_rect(topleft=self.shift_pos)

        func = lambda: print("pressed")
        # self.pos = pos
        # self.func = func
        #

    def mouse_collision(self, cors):
        return self.rect.collidepoint(cors) or self.shift_rect.collidepoint(cors)

    def draw(self):
        if not dom_event_manager.ishovered(self.id):
            self.screen.blit(self.surface, (self.pos[0], self.pos[1]))
        else:
            self.screen.blit(self.surface, (self.shift_pos[0], self.shift_pos[1]))
