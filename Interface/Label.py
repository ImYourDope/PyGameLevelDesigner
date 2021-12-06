from settings import *

from DOM.ElementInterface import ElementInterface


class Label(ElementInterface):
    DEFAULT = {
        'x': 0,
        'y': 0,
        'height': 30,
        'text': '',
    }

    def __init__(self, properties):
        self.id = properties['id']

        self.properties = properties

        self.text = properties['text']
        self.update_surface()

    def draw(self, screen):
        screen.blit(self.surface, (self.properties['x'], self.properties['y']))

    def update_surface(self):
        self.surface = main_font.render(self.text, False, main_font_color)

        # self.render = self.font.render(self.text, False, inputline_font_color)
        # self.render_rect = self.render.get_rect()
        # self.render_surface = pygame.Surface((self.render_rect.width + 7, self.render_rect.height))
        # self.render_surface.fill(inputline_background_color)
        # self.render_surface.blit(self.render, (0, 0))

    def mouse_collision(self, cors):
        return False # self.rect.collidepoint(cors)

    def setText(self, text):
        self.text = text
        self.update_surface()
