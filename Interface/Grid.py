from settings import *


class Grid:
    def __init__(self, canvas):
        self.canvas = canvas
        self.grid = pygame.Surface((self.canvas.width + 2, self.canvas.height + 2))
        self.grid.fill(grid_colorkey)

    def draw(self):
        for column in range(0, self.canvas.width_in_tiles + 1):
            pygame.draw.line(self.grid, grid_color, (column * tile_size, 0), (column * tile_size, self.canvas.height),
                             grid_thickness)
        for row in range(0, self.canvas.height_in_tiles + 1):
            pygame.draw.line(self.grid, grid_color, (0, row * tile_size), (self.canvas.width, row * tile_size),
                             grid_thickness)
        self.grid.set_colorkey(grid_colorkey)
        self.canvas.screen.blit(self.grid, (self.canvas.pos[0] - 1, self.canvas.pos[1] - 1))

    @staticmethod
    def toggle_grid(_):
        event_manager.grid_on = not event_manager.grid_on
        print(event_manager.grid_on)

