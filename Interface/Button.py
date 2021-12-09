import pygame

from settings import *
from DOM.ElementInterface import ElementInterface
from DOM.Layout import layout_manager


# class Button(ElementInterface):
#     DEFAULT = {
#         'x': 0,
#         'y': 0,
#         'width': 200,
#         'height': 28,
#         'align': {
#             'x': 'left',
#             'y': 'top'
#         },
#         'hover': {
#             'position': 'relative',
#             'x': 0,
#             'y': 0
#         }
#     }
#
#     def __init__(self, properties):
#         self.id = properties['id']
#         self.pos = (
#             properties['x'],
#             properties['y']
#         )
#         self.rect_size = (
#             properties['width'],
#             properties['height']
#         )
#
#         self.rect = pygame.Rect((
#             properties['x'],
#             properties['y'],
#             properties['width'],
#             properties['height']
#         ))
#
#         self.align = properties['align']
#
#     def align_shifting(self):
#
#         pos = [*self.pos]
#
#         width = self.rect_size[0]
#         height = self.rect_size[1]
#
#         if self.align['x'] == 'center':
#             pos[0] -= width / 2
#         elif self.align['x'] == 'right':
#             pos[0] -= width
#
#         if self.align['y'] == 'center':
#             pos[1] += height / 2
#         elif self.align['y'] == 'bottom':
#             pos[1] += height
#
#         return pos
#
#     def mouse_collision(self, pos):
#         return self.rect.collidepoint(pos)
#
#     def draw(self, screen):
#         pygame.draw.rect(screen, background_color, (self.rect_size, self.pos))
#         pygame.draw.rect(screen, popup_screen_border_color, (self.rect_size, self.pos), 2)

class Button(ElementInterface):
    DEFAULT = {
        'x': 0,
        'y': 0,
        'width': 200,
        'height': 28,
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
        self.rect_size = (properties['width'], properties['height'])
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

    # def rect_blitting_pos(self):
    #     pos = [*self.pos]
    #
    #     button_width = self.rect.width
    #     button_height = self.rect.height
    #
    #
    #     if self.align['x'] == 'center':
    #         pos[0] -= button_width / 2
    #     elif self.align['x'] == 'right':
    #         pos[0] -= button_width
    #
    #     if self.align['y'] == 'center':
    #         pos[1] += button_height / 2
    #     elif self.align['y'] == 'bottom':
    #         pos[1] += button_height
    #
    #     return pos

    def surface_blitting_pos(self):
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
            screen.blit(self.surface, self.surface_blitting_pos())
        else:
            screen.blit(self.surface, self.surface_blitting_pos())

        pygame.draw.rect(screen, popup_screen_border_color, (self.pos, self.rect_size), 2)
