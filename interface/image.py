import pygame.image

from dom.element_interface import ElementInterface


class Image(ElementInterface):
    DEFAULT = {
        'x': 0,
        'y': 0,
        'width': 100,
        'height': 100,
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
        self.pos = properties['x'], properties['y']
        self.size = properties['width'], properties['height']

        self.rect = pygame.Rect(
            self.pos,
            self.size
        )
        self.align = properties['align']
        self.properties = properties

    def surface_blitting_pos(self):
        pos = [*self.pos]

        width = self.rect.width
        height = self.rect.height

        if self.align['x'] == 'center':
            pos[0] -= width / 2
        elif self.align['x'] == 'right':
            pos[0] -= width

        if self.align['y'] == 'center':
            pos[1] -= height / 2
        elif self.align['y'] == 'bottom':
            pos[1] -= height

        return pos

    def update_image(self, surface):
        width = surface.get_width()
        height = surface.get_height()
        scale = min(self.properties['width'] / width, self.properties['height'] / height)
        self.surface = pygame.transform.scale(surface, (width * scale, height * scale))

    def draw(self, screen):
        if 'surface' in self.__dict__:
            screen.blit(self.surface, self.surface_blitting_pos())
