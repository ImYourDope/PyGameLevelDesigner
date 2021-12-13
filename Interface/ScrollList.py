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
        self.active = 0
        self.scroll_pos = 0
        self.surface = pygame.Surface((properties['width'], 10 ** 4))
        self.surface.set_colorkey('black')
        self.update_surface()
        self.align = properties['align']

    def tile_rect(self, i):
        tiles_per_row = 3
        width = 64
        height = 64
        padding_x = (self.rect.width - width * tiles_per_row) // (tiles_per_row + 1)
        padding_y = 20

        return pygame.Rect((
            i % tiles_per_row * (width + padding_x) + padding_x,
            i // tiles_per_row * (height + padding_y) + padding_y,
            width,
            height
        ))

    def update_surface(self):
        for i in range(100):
            pygame.draw.rect(self.surface, 'green' if self.active == i else 'blue', self.tile_rect(i))

    # def render_list(self, screen):
    #     for i in range(len(self.list)):
    #         screen.blit(self.list[i], ((i % 3) * 50, (i // 3) * 50))

    def draw(self, screen):
        sub_surface = self.surface.subsurface((0, self.scroll_pos), self.dimentions)
        screen.blit(sub_surface, self.pos)
        pygame.draw.rect(screen, popup_screen_border_color, (self.pos, self.dimentions), 2)

    def mouse_collision(self, cors):
        return self.rect.collidepoint(cors)

    def onclick(self, event):
        pos = [*event.pos]
        pos[0] -= self.pos[0]
        pos[1] -= self.pos[1] - self.scroll_pos
        for i in range(1000):
            if self.tile_rect(i).collidepoint(pos):
                self.active = i
        self.update_surface()

    def onscroll(self, event):
        if event.y > 0:
            self.scroll_pos -= 20
            self.scroll_pos = max(self.scroll_pos, 0)
        else:
            self.scroll_pos += 20
            self.scroll_pos = min(self.scroll_pos, 10 ** 3)
