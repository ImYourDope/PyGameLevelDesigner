import pygame
from dom import ElementInterface, layout_manager
from settings import main_font_name, main_font_color


class Label(ElementInterface):
    DEFAULT = {
        'x': 0,
        'y': 0,
        'height': 30,
        'text': '',
        'hover': {
            'position': 'relative',
            'x': 0,
            'y': 0
        },
        'align': {
            'x': 'left',
            'y': 'top'
        }
    }

    def __init__(self, properties):
        """Initializes the label."""

        self.id = properties['id']
        self.pos = (
            properties['x'],
            properties['y']
        )
        self.hover = properties['hover']
        self.font_size = properties['height']
        self.text = properties['text']
        self.align = properties['align']
        self.font_renderer = pygame.font.Font(main_font_name, self.font_size)
        self.update_surface()
        self.set_blitting_pos()

    def centering(self, pos):
        """Centers the label."""

        pos = [*pos]
        width = self.surface.get_width()
        height = self.surface.get_height()

        if self.align['x'] == 'center':
            pos[0] -= width / 2
        elif self.align['x'] == 'right':
            pos[0] -= width

        if self.align['y'] == 'center':
            pos[1] += height / 2
        elif self.align['y'] == 'bottom':
            pos[1] += height

        return pos

    def set_blitting_pos(self):
        """Decides which blitting position to use."""
        self.blitting_pos = self.centering(self.pos)

        if self.hover['position'] == 'absolute':
            self.hovered_blitting_pos = self.centering([self.hover['x'], self.hover['y']])
        elif self.hover['position'] == 'relative':
            pos = self.centering(self.pos)
            pos[0] += self.hover['x']
            pos[1] += self.hover['y']
            self.hovered_blitting_pos = pos
        else:
            raise Exception('Incorrect "position" attribute value')

    def draw(self, screen):
        """Draws the label."""

        if layout_manager.ishovered(self.id):
            screen.blit(self.surface, self.hovered_blitting_pos)
        else:
            screen.blit(self.surface, self.blitting_pos)

    def update_surface(self):
        """Updates the label."""

        self.surface = self.font_renderer.render(self.text, False, main_font_color)
        self.set_blitting_pos()

    def mouse_collision(self, pos):
        """Checks mouse collision with the label."""
        return self.surface.get_rect(topleft=self.blitting_pos).collidepoint(pos)

    def set_text(self, text):
        """Sets label's text."""
        self.text = text
        self.update_surface()
