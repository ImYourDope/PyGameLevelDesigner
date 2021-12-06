from settings import *
from DOM.ElementInterface import ElementInterface
from DOM.Layout import layout_manager


class Button(ElementInterface):
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

    def __init__(self, properties):
        self.id = properties['id']

        if properties['hover']['position'] == 'relative':
            properties['hover']['x'] += properties['x']
            properties['hover']['y'] += properties['y']

        self.surface = main_font.render(properties['text'], False, main_font_color)
        self.pos = (properties['x'], properties['y'])
        self.rect = self.surface.get_rect(topleft=self.pos)
        self.shift_pos = (properties['hover']['x'], properties['hover']['y'])
        self.shift_rect = self.surface.get_rect(topleft=self.shift_pos)

    def mouse_collision(self, cors):
        return self.rect.collidepoint(cors) or self.shift_rect.collidepoint(cors)

    def draw(self, screen):
        if not layout_manager.ishovered(self.id):
            screen.blit(self.surface, (self.pos[0], self.pos[1]))
        else:
            if self.id == 'save-tile':
                print("hello")
            screen.blit(self.surface, (self.shift_pos[0], self.shift_pos[1]))
