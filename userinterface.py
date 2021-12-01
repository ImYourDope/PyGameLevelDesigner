from settings import *

ui_rect = (0, 0, left_margin, screen_height)


def draw_ui_background(screen):
    screen.fill(background_color)


def draw_ui(screen):
    pygame.draw.rect(screen, ui_main_color, ui_rect)
    pygame.draw.rect(screen, ui_border_color, ui_rect, ui_border_thickness)
    pygame.draw.line(screen, ui_border_color, (0, ui_separation_line),
                     (left_margin, ui_separation_line), ui_border_thickness)

