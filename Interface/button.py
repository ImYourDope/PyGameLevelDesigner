import pygame.mouse

from settings import *
from .dom_element import DOMElement
from event_manager import dom_event_manager


class Button(DOMElement):
    def __init__(self, screen, properties):
        self.screen = screen
        self.id = properties['id']

        if 'x' not in properties:
            properties['x'] = 0
        if 'y' not in properties:
            properties['y'] = 0
        if 'width' not in properties:
            properties['width'] = 200
        if 'height' not in properties:
            properties['height'] = 30
        if 'text' not in properties:
            properties['text'] = ''

        if 'hover' in properties:
            if 'x' not in properties['hover']:
                properties['hover']['x'] = properties['x']
            if 'y' not in properties['hover']:
                properties['hover']['y'] = properties['y']

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