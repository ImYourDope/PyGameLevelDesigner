from buttonclass import Button
from canvas import *
from grid import *

main_buttons = []


def create_buttons(screen):
    main_buttons.append(Button(screen, 'GRID', (10, 10), grid_button, 15, 0))


buttons = main_buttons
