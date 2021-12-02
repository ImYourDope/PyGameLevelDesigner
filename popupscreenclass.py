from settings import *


class PopupScreen:
    def __init__(self, screen, rect, buttons_list, inputlines_list):
        self.screen = screen
        self.rect = pygame.Rect(rect)
        self.buttons = buttons_list
        self.inputlines = inputlines_list

    def draw(self):
        pygame.draw.rect(self.screen, popup_screen_background_color, self.rect)
        pygame.draw.rect(self.screen, popup_screen_border_color, self.rect, popup_screen_border_thickness)
        for i in self.inputlines:
            i.draw()
        for b in self.buttons:
            b.draw()

    def start(self):
        state['main_screen_on'] = False
        state['popup_screen_on'] = True
        state['active_buttons'] = self.buttons
        state['active_inputlines'] = self.inputlines
        state['popup_screen'] = self


def popup_screen_close():
        state['main_screen_on'] = True
        state['popup_screen_on'] = False
        state['active_buttons'] = main_screen_buttons
        state['active_inputlines'] = main_screen_inputlines
        state['popup_screen'] = None
