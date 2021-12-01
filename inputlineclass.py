from settings import *


class InputLine:
    def __init__(self, screen, rect, vocabulary):
        self.screen = screen
        self.rect = pygame.Rect(rect)
        self.vocabulary = vocabulary
        self.input = ''
        self.text = None
        self.text_rect = None
        self.text_surface = pygame.Surface((1, 1))
        self.selected = False
        self.font = pygame.font.Font(inputline_font, self.rect.height - 2 * inputline_border_thickness)

    def draw(self):
        pygame.draw.rect(self.screen, inputline_background_color, self.rect)
        pygame.draw.rect(self.screen, inputline_border_color, self.rect, inputline_border_thickness)
        self.screen.blit(self.text_surface.subsurface(self.text_surface.get_width()-min(self.rect.width - 4, self.text_surface.get_width()),
                                                      self.text_surface.get_height()-min(self.rect.height, self.text_surface.get_height()),
                                                      min(self.rect.width - 4, self.text_surface.get_width()),
                                                      min(self.rect.height, self.text_surface.get_height())),
                         (self.rect.x + inputline_border_thickness, self.rect.y + inputline_border_thickness))

    def update_text_surface(self):
        self.text = self.font.render(self.input, False, inputline_font_color)
        self.text_rect = self.text.get_rect()
        self.text_surface = pygame.Surface((self.text_rect.width + 7, self.text_rect.height))
        self.text_surface.fill(inputline_background_color)
        self.text_surface.blit(self.text, (0, 0))
        if self.selected:
            pygame.draw.line(self.text_surface, 'black', (self.text_rect.width + 4, 2),
                             (self.text_rect.width + 4, self.text_rect.height - 2), 3)

    def process(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.selected = True
                else:
                    self.selected = False

        if self.selected:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                elif event.unicode in self.vocabulary:
                    self.input += event.unicode

    def inputline_end(self, output):
        output = self.input
