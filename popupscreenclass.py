from inputlines import *


class PopUpScreen:
    def __init__(self, screen, rect, button_list, inputlines_list):
        self.screen = screen
        self.buttons = button_list
        self.inputlines = inputlines_list
        self.rect = pygame.Rect(rect)

    def draw(self):
        pygame.draw.rect(self.screen, popup_screen_background_color, self.rect)
        pygame.draw.rect(self.screen, popup_screen_border_color, self.rect, popup_screen_border_thickness)
        for i in self.inputlines:
            i.draw()
        for b in self.buttons:
            b.draw()

    def create(self):
        state['popup_screen'] = True
        state['main_screen'] = False
        popup_screen_buttons = self.buttons
        popup_screen_inputlines = self.inputlines
        popup_screen = self

