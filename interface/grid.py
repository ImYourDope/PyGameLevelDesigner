from settings import *



class Grid:
    def __init__(self, tile_width, tile_height):
        self.tile_size = (tile_width, tile_height)
        self.size = (tile_width * tile_size, tile_height * tile_size)

        self.grid = pygame.Surface(self.size)

    def draw(self, screen):
        self.grid.fill(grid_colorkey)

        for column in range(0, self.tile_size[0] + 1):
            pygame.draw.line(self.grid, grid_color, (column * tile_size, 0), (column * tile_size, self.size[1]),
                             grid_thickness)
        for row in range(0, self.tile_size[1] + 1):
            pygame.draw.line(self.grid, grid_color, (0, row * tile_size), (self.size[0], row * tile_size),
                             grid_thickness)

        self.grid.set_colorkey(grid_colorkey)
        screen.blit(self.grid, (0, 0))

    @staticmethod
    def tile_pos(pos):
        return (pos[0] - pos[0] % tile_size + grid_thickness,
                pos[1] - pos[1] % tile_size + grid_thickness)

    @staticmethod
    def toggle_grid(_):
        state_manager.set('grid on', not state_manager.get('grid on'))
