import pygame

from settings import *
from DOM import layout_manager, ElementInterface


class TextButton(ElementInterface):
    DEFAULT = {
        'x': 0,
        'y': 0,
        'text': '',
        'align': {
            'x': 'left',
            'y': 'top'
        },
        'hover': {
            'position': 'relative',
            'x': 0,
            'y': 0
        }
    }

    def __init__(self, properties):
        self.id = properties['id']

        if properties['hover']['position'] == 'relative':
            properties['hover']['x'] += properties['x']
            properties['hover']['y'] += properties['y']

        self.surface = main_font.render(properties['text'], False, main_font_color)
        self.pos = (properties['x'], properties['y'])
        self.rect_size = self.surface.get_size()
        self.rect = pygame.Rect(
            self.pos,
            self.rect_size
        )
        self.surface.get_rect(topleft=self.pos)
        self.shift_pos = (properties['hover']['x'], properties['hover']['y'])
        self.shift_rect = self.surface.get_rect(topleft=self.shift_pos)

        self.align = properties['align']

    def mouse_collision(self, cors):
        return self.rect.collidepoint(cors) or self.shift_rect.collidepoint(cors)

    def draw(self, screen):
        if not layout_manager.ishovered(self.id):
            screen.blit(self.surface, self.pos)
        else:
            screen.blit(self.surface, self.shift_pos)

    def set_text(self, text):
        self.surface = main_font.render(text, False, main_font_color)
