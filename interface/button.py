from dom import layout_manager, ElementInterface
from settings import *


class Button(ElementInterface):
    DEFAULT = {
        'x': 0,
        'y': 0,
        'width': 200,
        'height': 28,
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
        self.size = (properties['width'], properties['height'])
        self.rect = pygame.Rect(
            self.pos,
            self.size
        )
        hovered_pos = (properties['hover']['x'], properties['hover']['y'])
        self.hovered_rect = self.surface.get_rect(topleft=hovered_pos)

        self.align = properties['align']

    # def centering(self, pos):
    #     pos = [*pos]
    #     width = self.surface.get_width()
    #     height = self.surface.get_height()
    #
    #     if self.align['x'] == 'center':
    #         pos[0] -= width / 2
    #     elif self.align['x'] == 'right':
    #         pos[0] -= width
    #
    #     if self.align['y'] == 'center':
    #         pos[1] += height / 2
    #     elif self.align['y'] == 'bottom':
    #         pos[1] += height
    #
    #     return pos

    def mouse_collision(self, cors):
        return self.rect.collidepoint(cors)

    def blitting_pos(self):
        pos = [*self.pos]

        button_width = self.rect.width
        button_height = self.rect.height

        text_width = self.surface.get_width()
        text_height = self.surface.get_height()

        if self.align['x'] == 'center':
            pos[0] += (button_width - text_width) / 2
        elif self.align['x'] == 'right':
            pos[0] += button_width - text_width

        if self.align['y'] == 'center':
            pos[1] += (button_height - text_height) / 2
        elif self.align['y'] == 'bottom':
            pos[1] += button_height - text_height

        return pos

    def draw(self, screen):
        if not layout_manager.ishovered(self.id):
            screen.blit(self.surface, self.blitting_pos())
        else:
            screen.blit(self.surface, self.blitting_pos())

        pygame.draw.rect(screen, popup_screen_border_color, self.rect, 2)

    def set_text(self, text):
        self.surface = main_font.render(text, False, main_font_color)
