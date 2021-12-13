import pygame

from settings import *

from DOM.ElementInterface import ElementInterface


class ScrollList(ElementInterface):
    DEFAULT = {
        'x': 0,
        'y': 0,
        'width': 100,
        'height': 400,
        'text': '',
        'list': [],
        'align': {
            'x': 'left',
            'y': 'top'
        }
    }

    def __init__(self, properties):
        self.id = properties['id']

        self.properties = properties

        self.text = properties['text']
        self.list = properties['list']

        self.pos = (
            properties['x'],
            properties['y']
        )

        self.dimentions = (
            properties['width'],
            properties['height']
        )
        self.rect = pygame.Rect(
            self.pos,
            self.dimentions
        )
        self.scroll_pos = 0
        self.surface = pygame.Surface((properties['width'], 10**4))
        self.init_surface()
        self.align = properties['align']

    def init_surface(self):
        tiles_per_row = 1
        width = 300
        height = 48
        padding_x = (self.rect.width - width * tiles_per_row) // (tiles_per_row + 1)
        padding_y = 20
        for i in range(100):
            pygame.draw.rect(self.surface, 'red', (
                i % tiles_per_row * (width + padding_x) + padding_x,
                i // tiles_per_row * (height + padding_y) + padding_y,
                width,
                height
            ))

    def render_list(self, screen):
        for i in range(len(self.list)):
            screen.blit(self.list[i], ((i % 3) * 50, (i // 3) * 50))

    def draw(self, screen):
        print(self.scroll_pos)
        sub_surface = self.surface.subsurface((0, self.scroll_pos), self.dimentions)
        screen.blit(sub_surface, self.pos)

    def mouse_collision(self, cors):
        return self.rect.collidepoint(cors)

    def onclick(self, event):
        print('clicked')

    def onscroll(self, event):
        if event.y > 0:
            self.scroll_pos -= 10
            self.scroll_pos = max(self.scroll_pos, 0)
        else:
            self.scroll_pos += 10
            self.scroll_pos = min(self.scroll_pos, 10**3)


        print('scrolling')
