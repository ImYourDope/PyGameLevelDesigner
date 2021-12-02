import pygame

# MAIN SETTINGS
FPS = 60

# STATES
state = {
    'grid_on': True,
    'main_screen_on': True,
    'popup_screen_on': False,
    'active_inputlines': None,
    'active_buttons': None,
    'popup_screen': None
}

# FONT SETTINGS
pygame.font.init()
main_font_size = 30
main_font = pygame.font.Font('DisposableDroidBB_bld.ttf', main_font_size)
main_font_color = (255, 255, 255)


# SPRITESHEET SETTING
default_sprite_row_color = (255, 255, 0)
default_sprite_starting_color = (255, 0, 255)
default_sprite_ending_color = (0, 255, 255)
spritesheet_colorkey_color = (255, 255, 255)

# MAIN SCREEN SETTINGS
screen_width = 1400
screen_height = 700
top_margin = 0
bottom_margin = 0
left_margin = 400
right_margin = 0

# UI SETTINGS
ui_separation_line = 200
ui_main_color = (34, 52, 77)
ui_border_color = (54, 82, 120)
ui_border_thickness = 3

# CANVAS SETTINGS
canvas_default_color = (30, 100, 150)
canvas_pos = [left_margin, top_margin]
arrow_cursor_size = 30

# EDITING SCREEN SETTINGS
editing_screen_width = screen_width - left_margin - right_margin
editing_screen_height = screen_height - top_margin - bottom_margin
editing_screen_rect = pygame.Rect(left_margin, top_margin, editing_screen_width, editing_screen_height)
background_color = (9, 30, 45)

# GRID SETTINGS
grid_thickness = 2
grid_color = (255, 255, 255)
grid_colorkey = 'blue'

# SCROLLING SETTINGS
scrolling_margin = 100
void_margin = 120
top_scrolling_rect = pygame.Rect(left_margin + scrolling_margin, top_margin,
                                 editing_screen_width - 2 * scrolling_margin, scrolling_margin)
bottom_scrolling_rect = pygame.Rect(left_margin + scrolling_margin,
                                    top_margin + editing_screen_height - scrolling_margin,
                                    editing_screen_width - 2 * scrolling_margin, scrolling_margin)
left_scrolling_rect = pygame.Rect(left_margin, top_margin,
                                  scrolling_margin, editing_screen_height)
right_scrolling_rect = pygame.Rect(left_margin + editing_screen_width - scrolling_margin, top_margin,
                                   scrolling_margin, editing_screen_height)

# INPUTLINE SETTINGS
numbers_vocabulary = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
letters_vocabulary = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
capital_letters_vocabulary = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
symbols_vocabulary = ('_', '-', "'", '@', '#')
inputline_vocabulary = numbers_vocabulary + letters_vocabulary + capital_letters_vocabulary + symbols_vocabulary
inputline_background_color = (255, 255, 255)
inputline_border_color = ui_border_color
inputline_border_thickness = 2
inputline_font = 'DisposableDroidBB_bld.ttf'
inputline_font_size = main_font_size
inputline_font_color = (0, 0, 0)
main_screen_inputlines = []
test_popup_screen_inputlines = []

# BUTTONS SETTINGS
main_screen_buttons = []
test_popup_screen_buttons = []
button_gap = -2
starting_button_pos = 5

# POPUPSCREEN SETTINGS
popup_screen_background_color = ui_main_color
popup_screen_border_color = ui_border_color
popup_screen_border_thickness = 2
