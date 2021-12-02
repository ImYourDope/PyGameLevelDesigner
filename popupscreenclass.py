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
        event_manager.main_screen_on = False
        event_manager.popup_screen_on = True
        event_manager.active_buttons = self.buttons
        event_manager.active_inputlines = self.inputlines
        event_manager.popup_screen = self

    def open(self):
        print('opened')


def popup_screen_close():
        event_manager.main_screen_on = True
        event_manager.popup_screen_on = False
        event_manager.active_buttons = main_screen_buttons
        event_manager.active_inputlines = main_screen_inputlines
        event_manager.popup_screen = None
