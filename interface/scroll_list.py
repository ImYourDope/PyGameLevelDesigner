from dom.element_interface import ElementInterface
from settings import *


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
        self.search_string = ''

        self.pos = (
            properties['x'],
            properties['y']
        )

        self.size = (
            properties['width'],
            properties['height']
        )
        self.rect = pygame.Rect(
            self.pos,
            self.size
        )
        self.font = pygame.font.Font(main_font_name, 20)

        self.tiles_per_row = 4
        self.width = 64
        self.height = 64
        self.padding_x = (self.rect.width - self.width * self.tiles_per_row) // (self.tiles_per_row + 1)
        self.padding_y = 20
        self.active = None
        self.scroll_pos = 0
        self.surface = pygame.Surface((properties['width'], 10 ** 4))
        self.surface.set_colorkey('white')
        self.update_surface()
        self.align = properties['align']

    def tile_pos(self, i):
        return (
            i % self.tiles_per_row * (self.width + self.padding_x) + self.padding_x,
            i // self.tiles_per_row * (self.height + self.padding_y) + self.padding_y,
        )

    def tile_rect(self, i):
        return pygame.Rect(self.tile_pos(i), (self.width, self.height))

    def append(self, tile, name):
        self.list.append([tile, name])

    def update_surface(self):
        for i in range(len(self.list)):
            self.list[i][0] = scale(self.list[i][0], self.width, self.height)

        active_list = []
        for (tile, name) in self.list:
            if self.search_string in name:
                active_list.append((tile, name))

        self.surface.fill('white')
        for i in range(len(active_list)):
            tile = active_list[i][0]
            name = active_list[i][1]
            self.surface.blit(tile, self.tile_pos(i))

            text = self.font.render(name, False, (254, 255, 255))

            text_pos = self.tile_pos(i)
            self.surface.blit(text, (
                text_pos[0],
                text_pos[1] + self.height
            ))
            if self.active == i:
                pygame.draw.rect(self.surface, 'green', self.tile_rect(i), 2)

    def set_search(self, search_string):
        self.search_string = search_string
        self.update_surface()

    def draw(self, screen):
        sub_surface = self.surface.subsurface((0, self.scroll_pos), self.size)
        screen.blit(sub_surface, self.pos)
        pygame.draw.rect(screen, popup_screen_border_color, (self.pos, self.size), ui_border_thickness)

    def mouse_collision(self, cors):
        return self.rect.collidepoint(cors)

    def selected_tile(self):
        if self.active is not None:
            return self.list[self.active][0]
        return None

    def selected_name(self):
        if self.active is not None:
            return self.list[self.active][1]
        return None

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
