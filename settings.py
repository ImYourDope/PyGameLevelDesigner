import pygame

# MAIN SETTINGS
FPS = 60

# FONT SETTINGS
pygame.font.init()
main_font = pygame.font.Font('ARCADECLASSIC.TTF', 24)
font_color = (255, 255, 255)

# SPRITESHEET SETTING
default_sprite_row_color = (255, 255, 0)
default_sprite_starting_color = (255, 0, 255)
default_sprite_ending_color = (0, 255, 255)
spritesheet_colorkey_color = (255, 255, 255)

# MAIN SCREEN SETTINGS
screen_width = 1300
screen_height = 700
upper_margin = 0
lower_margin = 0
left_margin = 300
right_margin = 0
editing_screen_width = screen_width - left_margin - right_margin
editing_screen_height = screen_height - upper_margin - lower_margin

# UI SETTINGS
ui_separation_line = 150
ui_main_color = (34, 52, 77)
ui_border_color = (54, 82, 120)
ui_border_thickness = 3

# EDITING SCREEN SETTINGS
background_color = (3, 10, 25)
canvas_pos = (left_margin, 0)
grid_thickness = 2
grid_color = (255, 255, 255)
grid_colorkey = 'blue'
