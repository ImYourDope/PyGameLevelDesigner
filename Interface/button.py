from settings import *


class Button:
    def __init__(self, screen, properties):
        self.screen = screen

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

        if 'hover' in properties:
            if 'x' not in properties['hover']:
                properties['hover']['x'] = properties['x']
            if 'y' not in properties['hover']:
                properties['hover']['y'] = properties['y']



        self.surface = main_font.render(properties['text'], False, main_font_color)
        self.pos = (properties['x'], properties['y'])
        self.rect = self.surface.get_rect(topleft=self.pos)
        self.shift_pos = (properties['hover']['x'], properties['hover']['y'])
        self.shift_rect = self.surface.get_rect(topleft=self.shift_pos)

        func = lambda: print("pressed")
        # self.pos = pos
        # self.func = func
        #

    def mouse_collision(self):
        return self.rect.collidepoint(pygame.mouse.get_pos()) or self.shift_rect.collidepoint(pygame.mouse.get_pos())

    def draw(self):
        if not self.mouse_collision():
            self.screen.blit(self.surface, (self.pos[0], self.pos[1]))
        else:
            self.screen.blit(self.surface, (self.shift_pos[0], self.shift_pos[1]))

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.mouse_collision():
                    self.func()
