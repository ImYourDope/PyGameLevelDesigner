from playerinput import *
from settings import *

grid = pygame.Surface((canvas_width, canvas_height))
grid.fill(grid_colorkey)
grid_on = True


def grid_button():
    global grid_on
    grid_on = not grid_on
    # print(grid_on)


def draw_grid(screen):
    for column in range(0, canvas_width_in_tiles):
        pygame.draw.line(grid, grid_color, (column * tile_size, 0), (column * tile_size, canvas_height), grid_thickness)
    for row in range(0, canvas_height_in_tiles):
        pygame.draw.line(grid, grid_color, (0, row * tile_size), (screen_width, row * tile_size), grid_thickness)
    grid.set_colorkey(grid_colorkey)
    screen.blit(grid, (canvas_pos[0], canvas_pos[1]))
