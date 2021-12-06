from DOM.ElementInterface import ElementInterface
from userinput import *
from settings import *

grid = pygame.Surface((canvas_width + 2, canvas_height + 2))
grid.fill(grid_colorkey)


class Grid(ElementInterface):
    def __init__(self, properties):
        pass

    def draw(self, screen):
        for column in range(0, canvas_width_in_tiles + 1):
            pygame.draw.line(grid, grid_color, (column * tile_size, 0), (column * tile_size, canvas_height),
                             grid_thickness)
        for row in range(0, canvas_height_in_tiles + 1):
            pygame.draw.line(grid, grid_color, (0, row * tile_size), (canvas_width, row * tile_size), grid_thickness)
        grid.set_colorkey(grid_colorkey)
        screen.blit(grid, (canvas_pos[0] - 1, canvas_pos[1] - 1))

    def mouse_collision(self, pos):
        return False

    def toggle_grid(self, e):
        eventManager.grid_on = not eventManager.grid_on
