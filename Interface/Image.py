from DOM.ElementInterface import ElementInterface


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
        self.properties = properties

    def update_image(self, surface):
        self.surface = surface

    def draw(self, screen):
        if 'surface' in self.__dict__:
            screen.blit(self.surface, self.pos)
