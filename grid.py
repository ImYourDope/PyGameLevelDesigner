from userinput import *
from settings import *

grid = pygame.Surface((canvas_width + 2, canvas_height + 2))
grid.fill(grid_colorkey)


def grid_button():
    event_manager.grid_on = not event_manager.grid_on


def draw_grid(screen):
    for column in range(0, canvas_width_in_tiles + 1):
        pygame.draw.line(grid, grid_color, (column * tile_size, 0), (column * tile_size, canvas_height), grid_thickness)
    for row in range(0, canvas_height_in_tiles + 1):
        pygame.draw.line(grid, grid_color, (0, row * tile_size), (canvas_width, row * tile_size), grid_thickness)
    grid.set_colorkey(grid_colorkey)
    screen.blit(grid, (canvas_pos[0]-1, canvas_pos[1]-1))
