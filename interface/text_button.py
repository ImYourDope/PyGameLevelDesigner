from dom import layout_manager, ElementInterface
from settings import *


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
        self.size = self.surface.get_size()
        self.rect = pygame.Rect(
            self.pos,
            self.size
        )

        self.hovered_pos = (properties['hover']['x'], properties['hover']['y'])
        self.hovered_rect = self.surface.get_rect(topleft=self.hovered_pos)

        self.align = properties['align']

    def mouse_collision(self, cors):
        return self.rect.collidepoint(cors) or self.hovered_rect.collidepoint(cors)

    def draw(self, screen):
        if not layout_manager.ishovered(self.id):
            screen.blit(self.surface, self.pos)
        else:
            screen.blit(self.surface, self.hovered_pos)

    def set_text(self, text):
        self.surface = main_font.render(text, False, main_font_color)
