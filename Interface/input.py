from settings import *

from .dom_element import DOMElement
from event_manager import dom_event_manager


class Input(DOMElement):
    def __init__(self, screen, properties, vocabulary="abcdefghijklmnopqrstuvwxyz"):
        self.screen = screen
        self.id = properties['id']

        if 'x' not in properties:
            properties['x'] = 0
        if 'y' not in properties:
            properties['y'] = 0
        if 'width' not in properties:
            properties['width'] = 200
        if 'height' not in properties:
            properties['height'] = 30
        if 'text' not in properties:
            properties['text'] = ''

        self.rect = pygame.Rect(properties['x'],
                                properties['y'],
                                properties['width'],
                                properties['height'])
        self.vocabulary = vocabulary
        self.input = ''
        self.text = None
        self.text_rect = None
        self.text_surface = pygame.Surface((1, 1))
        self.font = pygame.font.Font(inputline_font, self.rect.height - 2 * inputline_border_thickness)

    def draw(self):
        pygame.draw.rect(self.screen, inputline_background_color, self.rect)
        pygame.draw.rect(self.screen, inputline_border_color, self.rect, inputline_border_thickness)
        self.screen.blit(self.text_surface.subsurface(
            self.text_surface.get_width() - min(self.rect.width - 4, self.text_surface.get_width()),
            self.text_surface.get_height() - min(self.rect.height, self.text_surface.get_height()),
            min(self.rect.width - 4, self.text_surface.get_width()),
            min(self.rect.height, self.text_surface.get_height())),
            (self.rect.x + inputline_border_thickness, self.rect.y + inputline_border_thickness))

    def update_text_surface(self):
        self.text = self.font.render(self.input, False, inputline_font_color)
        self.text_rect = self.text.get_rect()
        self.text_surface = pygame.Surface((self.text_rect.width + 7, self.text_rect.height))
        self.text_surface.fill(inputline_background_color)
        self.text_surface.blit(self.text, (0, 0))
        if dom_event_manager.infocus(self.id):
            pygame.draw.line(self.text_surface, 'black', (self.text_rect.width + 4, 2),
                             (self.text_rect.width + 4, self.text_rect.height - 2), 3)

    def mouse_collision(self, cors):
        return self.rect.collidepoint(cors)

    def oninput(self, event):
        if event.key == pygame.K_BACKSPACE:
            self.input = self.input[:-1]
        elif event.unicode in self.vocabulary:
            self.input += event.unicode

        self.update_text_surface()

    def inputline_end(self, output):
        output = self.input
