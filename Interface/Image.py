from DOM.ElementInterface import ElementInterface


class Image(ElementInterface):
    DEFAULT = {}

    def __init__(self, properties):
        self.id = properties['id']
        self.pos = properties['x'], properties['y']
        self.properties = properties

    def update_image(self, surface):
        self.surface = surface

    def draw(self, screen):
        if 'surface' in self.__dict__:
            screen.blit(self.surface, self.pos)
