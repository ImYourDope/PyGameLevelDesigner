from playerinput import *
from settings import *

canvas = pygame.Surface((canvas_width, canvas_height))
canvas.fill('green')


def draw_canvas(screen):
    screen.blit(canvas, (canvas_pos[0], canvas_pos[1]))
