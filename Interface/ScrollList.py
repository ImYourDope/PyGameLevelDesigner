import pygame

from settings import *

from DOM.ElementInterface import ElementInterface


def scale(surface, width, height):
    surface_width = surface.get_width()
    surface_height = surface.get_height()
    surface_scale = min(width / surface_width, height / surface_height)
    return pygame.transform.scale(surface, (surface_width * surface_scale, surface_height * surface_scale))


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

        self.tiles_per_row = 4
        self.width = 64
        self.height = 64
        self.padding_x = (self.rect.width - self.width * self.tiles_per_row) // (self.tiles_per_row + 1)
        self.padding_y = 20
        self.active = None
        self.scroll_pos = 0
        self.surface = pygame.Surface((properties['width'], 10 ** 4))
        self.surface.set_colorkey('black')
        self.update_surface()
        self.align = properties['align']

    def tile_pos(self, i):
        return (
            i % self.tiles_per_row * (self.width + self.padding_x) + self.padding_x,
            i // self.tiles_per_row * (self.height + self.padding_y) + self.padding_y,
        )

    def tile_rect(self, i):
        return pygame.Rect(self.tile_pos(i), (self.width, self.height))

    def update_surface(self):
        for i in range(len(self.list)):
            self.list[i] = scale(self.list[i], self.width, self.height)

        self.surface.fill('black')
        for i in range(len(self.list)):
            self.surface.blit(self.list[i], self.tile_pos(i))
            if self.active == i:
                pygame.draw.rect(self.surface, 'green', self.tile_rect(i), 2)

    def draw(self, screen):
        sub_surface = self.surface.subsurface((0, self.scroll_pos), self.dimentions)
        screen.blit(sub_surface, self.pos)
        pygame.draw.rect(screen, popup_screen_border_color, (self.pos, self.dimentions), ui_border_thickness)

    def mouse_collision(self, cors):
        return self.rect.collidepoint(cors)

    def onclick(self, event):
        pos = [*event.pos]
        pos[0] -= self.pos[0]
        pos[1] -= self.pos[1] - self.scroll_pos
        for i in range(len(self.list)):
            if self.tile_rect(i).collidepoint(pos):
                self.active = i
                break
        else:
            self.active = None
        self.update_surface()

    def onscroll(self, event):
        if event.y > 0:
            self.scroll_pos -= 20
            self.scroll_pos = max(self.scroll_pos, 0)
        else:
            self.scroll_pos += 20
            self.scroll_pos = min(self.scroll_pos, 10 ** 3)
