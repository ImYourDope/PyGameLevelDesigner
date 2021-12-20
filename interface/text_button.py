from dom import layout_manager, ElementInterface, layout
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
        state_manager.set(self.id+'state', False)
        self.text = properties['text']

        if properties['hover']['position'] == 'relative':
            properties['hover']['x'] += properties['x']
            properties['hover']['y'] += properties['y']

        state_manager.set(self.id+'surface', main_font.render(self.text, False, main_font_color))
        self.pos = (properties['x'], properties['y'])
        self.size = state_manager.get(self.id+'surface').get_size()
        self.rect = pygame.Rect(
            self.pos,
            self.size
        )

        self.hovered_pos = (properties['hover']['x'], properties['hover']['y'])
        self.hovered_rect = state_manager.get(self.id+'surface').get_rect(topleft=self.hovered_pos)
        self.align = properties['align']

    def mouse_collision(self, cors):
        return self.rect.collidepoint(cors) or self.hovered_rect.collidepoint(cors)

    def draw(self, screen):
        if not layout_manager.ishovered(self.id) or not state_manager.get(self.id+'state'):
            screen.blit(state_manager.get(self.id+'surface'), self.pos)
        else:
            screen.blit(state_manager.get(self.id+'surface'), self.hovered_pos)

    def set_text(self, text):
        state_manager.set(self.id+'surface', main_font.render(text, False, main_font_color))

    def update(self):
        if state_manager.get(self.id+'state'):
            state_manager.set(self.id + 'surface', main_font.render(self.text, False, main_font_color))
        else:
            state_manager.set(self.id + 'surface', main_font.render(self.text, False, inactive_font_color))


