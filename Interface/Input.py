from settings import *

from DOM.ElementInterface import ElementInterface
from DOM.Layout import layout_manager

class Input(ElementInterface):
    DEFAULT = {
        'x': 0,
        'y': 0,
        'width': 200,
        'height': 30,
        'text': '',
        'type': 'text'
    }

    def __init__(self, properties):
        self.id = properties['id']

        self.rect = pygame.Rect(properties['x'],
                                properties['y'],
                                properties['width'],
                                properties['height'])
        self.vocabulary = inputline_vocabulary
        self.text = properties['text']
        self.render = None
        self.render_rect = None
        self.render_surface = pygame.Surface((1, 1))
        self.font = pygame.font.Font(inputline_font, self.rect.height - 2 * inputline_border_thickness)

    def draw(self, screen):
        self.update_surface()

        pygame.draw.rect(screen, inputline_background_color, self.rect)
        pygame.draw.rect(screen, inputline_border_color, self.rect, inputline_border_thickness)
        screen.blit(self.render_surface.subsurface(
            self.render_surface.get_width() - min(self.rect.width - 4, self.render_surface.get_width()),
            self.render_surface.get_height() - min(self.rect.height, self.render_surface.get_height()),
            min(self.rect.width - 4, self.render_surface.get_width()),
            min(self.rect.height, self.render_surface.get_height())),
            (self.rect.x + inputline_border_thickness, self.rect.y + inputline_border_thickness))

    def update_surface(self):
        self.render = self.font.render(self.text, False, inputline_font_color)
        self.render_rect = self.render.get_rect()
        self.render_surface = pygame.Surface((self.render_rect.width + 7, self.render_rect.height))
        self.render_surface.fill(inputline_background_color)
        self.render_surface.blit(self.render, (0, 0))
        if layout_manager.infocus(self.id):
            pygame.draw.line(self.render_surface, 'black', (self.render_rect.width + 4, 2),
                             (self.render_rect.width + 4, self.render_rect.height - 2), 3)



    def mouse_collision(self, cors):
        return self.rect.collidepoint(cors)

    def onfocus(self, event):
        self.update_surface()

    def onunfocus(self, event):
        self.update_surface()

    def oninput(self, event):
        if event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        elif event.unicode in self.vocabulary:
            self.text += event.unicode

        self.update_surface()

    def inputline_end(self, output):
        output = self.text
