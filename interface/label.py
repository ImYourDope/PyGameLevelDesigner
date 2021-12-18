import pygame

from dom import ElementInterface, layout_manager
from settings import main_font_name, main_font_color


class Label(ElementInterface):
    DEFAULT = {
        'x': 0,
        'y': 0,
        'height': 30,
        'text': '',
        'hover': {
            'position': 'relative',
            'x': 0,
            'y': 0
        },
        'align': {
            'x': 'left',
            'y': 'top'
        }
    }

    def __init__(self, properties):
        self.id = properties['id']

        self.pos = (
            properties['x'],
            properties['y']
        )
        self.hover = properties['hover']
        self.font_size = properties['height']
        self.text = properties['text']
        self.align = properties['align']

        self.font_renderer = pygame.font.Font(main_font_name, self.font_size)

        self.update_surface()
        self.set_blitting_pos()

    def centering(self, pos):
        pos = [*pos]
        width = self.surface.get_width()
        height = self.surface.get_height()

        if self.align['x'] == 'center':
            pos[0] -= width / 2
        elif self.align['x'] == 'right':
            pos[0] -= width

        if self.align['y'] == 'center':
            pos[1] += height / 2
        elif self.align['y'] == 'bottom':
            pos[1] += height

        return pos

    def set_blitting_pos(self):
        self.blitting_pos = self.centering(self.pos)

        if self.hover['position'] == 'absolute':
            self.hovered_blitting_pos = self.centering([self.hover['x'], self.hover['y']])
        elif self.hover['position'] == 'relative':
            pos = self.centering(self.pos)

            pos[0] += self.hover['x']
            pos[1] += self.hover['y']

            self.hovered_blitting_pos = pos
        else:
            raise Exception('Incorrect "position" attribute value')

    def draw(self, screen):
        if layout_manager.ishovered(self.id):
            screen.blit(self.surface, self.hovered_blitting_pos)
        else:
            screen.blit(self.surface, self.blitting_pos)

    def update_surface(self):
        self.surface = self.font_renderer.render(self.text, False, main_font_color)

    def mouse_collision(self, pos):
        return self.surface.get_rect(topleft=self.blitting_pos).collidepoint(pos)

    def set_text(self, text):
        self.text = text
        self.update_surface()
