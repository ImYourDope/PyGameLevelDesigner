import pygame
from settings import *
from canvas import *


class Button:
    def __init__(self, screen, text, pos, func, x_shift, y_shift):
        self.screen = screen
        self.surface = main_font.render(text, False, font_color)
        self.pos = pos
        self.func = func
        self.shift_pos = (pos[0] + x_shift, pos[1] + y_shift)
        self.rect = self.surface.get_rect(topleft=self.pos)
        self.shift_rect = self.surface.get_rect(topleft=self.shift_pos)

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